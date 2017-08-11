# coding: utf-8

import pygame, sys, os
from pygame.locals import *

# # is Wall
# $ is Box
# @ is Man
# - is Space
# . is Target Point
# * is Box with Target Point
# + is Man with Target Point

def move_box(level, i):
    if level[i] == '-' or level[i] == '@':
        level[i] = '$'
    else:
        level[i] = '*'

def move_man(level, i):
    if level[i] == '-' or level[i] == '$':
        level[i] = '@'
    else:
        level[i] = '+'

def move_floor(level, i): # Reset Space/TP after Man/Box leaves
    if level[i] == '@' or level[i] == '$':
        level[i] = '-'
    else:
        level[i] = '.'

def get_offset(d, wid): # d for direction & width of the game screen 
    offset_ope = {'l': -1, 'u': -wid, 'r': 1, 'd': wid}
    return offset_ope[d.lower()]

class Boxpushing:
    def __init__(self):
        self.level = list(
                "----#####----------"
                "----#---#----------"
                "----#$--#----------"           
                "--###--$##---------"
                "--#--$-$-#---------"
                "###-#-##-#---######"
                "#---#-##-#####--..#"
                "#-$--$----------..#"       
                "#####-###-#@##--..#"
                "----#------########"                                 
                "----#######--------")

        self.w = 19  # columns x
        self.h = 11  # lines y
        self.man = 163  # ori pos of man

        self.solution = [] # records of every mvments
        self.push = 0 # times of pushing boxes
        self.todo = [] # to redo

    def draw(self, screen, skin):
        wd = skin.get_width() / 4 # width of each pic element
        
        for i in range(0, self.w):
            for j in range(0, self.h):
                item = self.level[j*self.w + i]
                if item == '#':
                    screen.blit(skin, (i*wd, j*wd), (0, 2*wd, wd, wd))
                elif item == '-':
                    screen.blit(skin, (i*wd, j*wd), (0, 0, wd, wd))
                elif item == '$':
                    screen.blit(skin, (i*wd, j*wd), (2*wd, 0, wd, wd))
                elif item == '@':
                    screen.blit(skin, (i*wd, j*wd), (wd, 0, wd, wd))
                elif item == '.':
                    screen.blit(skin, (i*wd, j*wd), (0, wd, wd, wd))
                elif item == '*':
                    screen.blit(skin, (i*wd, j*wd), (2*wd, wd, wd, wd))
                elif item == '+':
                    screen.blit(skin, (i*wd, j*wd), (wd, wd, wd, wd))
    
    def move(self, d):
        self._move(d)
        self.todo = [] # clear todo[] again and again...

    def _move(self, d):
        h = get_offset(d, self.w)
                     
        if self.level[self.man + h] == '-' or self.level[self.man + h] == '.':
            move_man(self.level, self.man + h)
            move_floor(self.level, self.man)
            self.man += h
            self.solution += d

        elif self.level[self.man + h] == '$' or self.level[self.man + h] == '*':
            h2 = h * 2
            if self.level[self.man + h2] == '-' or self.level[self.man + h2] == '.': # only next step is Space or TP, then move
                move_box(self.level, self.man + h2)
                move_man(self.level, self.man + h)
                move_floor(self.level, self.man)
                self.man += h
                self.solution += d.upper()
                self.push += 1

    def undo(self):
        if self.solution.__len__() > 0:
            self.todo.append(self.solution[-1]) # add the last step to todo[]
            self.solution.pop() # del the last step in solution[]
            
            h = get_offset(self.todo[-1], self.w) * -1 # reverse displacement
            if self.todo[-1].islower(): # use upper/lower() to judge whether Man has pushed Boxes
                move_man(self.level, self.man + h)
                move_floor(self.level, self.man)
                self.man += h 
                # No addition of self.solution
            else: # pushed boxes
                move_floor(self.level, self.man - h)
                move_box(self.level, self.man)
                move_man(self.level, self.man + h)
                self.man += h
                self.push -= 1
    
    def redo(self):
        if self.todo.__len__() > 0:
            self._move(self.todo[-1].lower())
            self.todo.pop()

# Finally... maybe Originally...
def main():
    pygame.init()
    screen = pygame.display.set_mode((400,300))

    skinfilename = os.path.join('/Users/yangyaoxian/Desktop/pythoncodes/pycodes/PythonWheels-master/boxpusher/borgar.png')
    try:
        skin = pygame.image.load(skinfilename)
    except pygame.error as msg:
        print ('cannot load skin')
        raise SystemExit(msg)
    skin = skin.convert()

    screen.fill(skin.get_at((0,0)))
    pygame.display.set_caption('The Great Boxpusher')
    bxp = Boxpushing()
    bxp.draw(screen, skin)

    clock = pygame.time.Clock()
    pygame.key.set_repeat(200,50)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    bxp.move('l')
                    bxp.draw(screen,skin)
                elif event.key == K_RIGHT:
                    bxp.move('r')
                    bxp.draw(screen,skin)
                elif event.key == K_UP:
                    bxp.move('u')
                    bxp.draw(screen,skin)
                elif event.key == K_DOWN:
                    bxp.move('d')
                    bxp.draw(screen,skin)
                elif event.key == K_BACKSPACE:
                    bxp.undo()
                    bxp.draw(screen,skin)
                elif event.key == K_SPACE:
                    bxp.redo()
                    bxp.draw(screen,skin)

        pygame.display.update()
            
        pygame.display.set_caption(bxp.solution.__len__().__str__() + '/' + bxp.push.__str__() + '   ' + 'The Great Boxpusher')


if __name__ == '__main__':
    main()
