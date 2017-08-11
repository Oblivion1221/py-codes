import os
import sys
import pyprind
import tty
import termios
import time
import threading
import cv2

class CharFrame:
    ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    def mapPixel(self, luminance):                                                           # map pixels to chars
        return self.ascii_char[int(luminance / 256 * len(self.ascii_char))]
    def convertToCharFrame(self, img, limitsize = -1, fill = False, wrap = False):           # fill: use <space> to fill the widths of frames to reach the limit width;
        if limitsize != -1 and (img.shape[0] > limitsize[1] or img.shape[1] > limitsize[0]): # wrap: switch to the next line
            img = cv2.resize(img, limitsize, interpolation = cv2.INTER_AREA)
        ascii_frame = ' '
        blanks = ''
        if fill:
            blanks += ' ' * (limitsize[0] - img.shape[1])
        if wrap:
            blanks += '\n'
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                ascii_frame += self.mapPixel(img[i, j])
            ascii_frame += blanks
        return ascii_frame

class V2Char(CharFrame):
    charVideo = []  # store the results
    timeInterval = 0.033

    def __init__(self, path):
        if path.endswith('txt'):
            self.load(path)
        else:
            self.genCharVideo(path)

    def genCharVideo(self, filepath):
        self.charVideo = []
        cap = cv2.VideoCapture(filepath)
        self.timeInterval = round(1/cap.get(5), 3)
        nf = int(cap.get(7))                                                                 # This must be int because pyprind.prog_bar() take an 'int' type parameter
        print('Generate char video, please wait...')
        for i in pyprind.prog_bar(range(nf)):
            rawFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
            frame = self.convertToCharFrame(rawFrame, os.get_terminal_size(), fill = True)
            self.charVideo.append(frame)
        cap.release()

    def load(self, filepath):
        self.charVideo = []
        # 1 line for 1 frame
        for i in open(filepath):
            self.charVideo.append(i[:-1])

    def export(self, filepath):
        if not self.charVideo:
            return
        with open(filepath, 'w') as f:
            for frame in self.charVideo:
                f.write(frame + '\n')

    def play(self, stream = 1):
        if not self.charVideo:
            return
        if stream == 1 and os.isatty(sys.stdout.fileno()):
            self.streamOut = sys.stdout.write                                                # define streamOut/Flush as sys.stdout.write/flush. No ()
            self.streamFlush = sys.stdout.flush
        elif stream == 2 and os.isatty(sys.stderr.fileno()):
            self.streamOut = sys.stderr.write
            self.streamFlush = sys.stderr.flush
        elif hasattr(stream, 'write'):
            self.streamOut = stream.write
            self.streamFlush = stream.flush

        old_settings = None
        breakflag = None
        fd = sys.stdin.fileno()

        def getChar():                                                                       # simulate getchar() in C in order to exit when there's an user input
            nonlocal old_settings
            nonlocal breakflag

            old_settings = termios.tcgetattr(fd)
            tty.setraw(sys.stdin.fileno())
            c = sys.stdin.read(1)
            breakflag = True if c else False

        getchar = threading.Thread(target=getChar)
        getchar.daemon = True
        getchar.start()
        rows = len(self.charVideo[0]) // os.get_terminal_size()[0]                           # //: divide with integral result (discard remainder); 1 index for 1 frame; get_terminal_size()[0] returns the number of columns
        for frame in self.charVideo:
            if breakflag:
                break
            self.streamOut(frame)
            self.streamFlush()
            time.sleep(self.timeInterval)                                                    # print each frame with the interval of timeInterval secs
            self.streamOut('\033[{}A\r'.format(rows - 1))

        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)                               # switch input attribute back to old_settings
        self.streamOut('\033[{}B\033[K'.format(rows - 1))
        for i in range(rows - 1):
            self.streamOut('\033[1A')
            self.streamOut('\r\033[K')
        info = 'User Interrupted!\n' if breakflag else 'Done~\n'
        self.streamOut(info)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                        help='Video file or charvideo file')
    parser.add_argument('-e', '--export', nargs='?', const='charvideo.txt',
                        help='Export charvideo file')

    args = parser.parse_args()
    v2char = V2Char(args.file)
    if args.export:
        v2char.export(args.export)
    v2char.play()
