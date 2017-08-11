import cv2


class BlackWhiteConvert:
    def __init__(self, path):
        cap = cv2.VideoCapture(path)
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')                                                    # bugs in macOS
        out = cv2.VideoWriter('/Users/yangyaoxian/Downloads/output.avi', fourcc, 20.0, (1280, 720))
        success, frame = cap.read()
        while success:
            rawframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            res = self.convert(rawframe)
            out.write(res)
            success, frame = cap.read()
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def convert(self, img):
        img[img != 0] = 255
        return img


if __name__ == '__main__':
    BlackWhiteConvert('/Users/yangyaoxian/Downloads/10451356-1.mp4')