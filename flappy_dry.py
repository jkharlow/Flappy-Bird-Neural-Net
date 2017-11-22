from itertools import cycle
import random
import sys
import pygame
import csv
from pygame.locals import *

#   VARIABLES
FPS = 30
SCREENWIDTH = 288
SCREENHEIGHT = 512
PIPEGAPSIZE  = 150 # gap between upper and lower part of pipe
BASEY = SCREENHEIGHT * 0.79
PIPEDETERMINTISIC = False
DISPLAYSCREEN = True
DisplayGraphics = True
IMAGES, SOUNDS, HITMASKS = {}, {}, {} # image, sound and hitmask  dicts

player = None

#   sizes
backg_width = 288
backg_height = 512
base_width = 336
base_height = 112
pipe_width = 52
pipe_height = 320
bird_width = 34
bird_height = 24

#   records
dx_pipe =[]
location = []
#   END VARS


class Bird:
    ''' Defines the player object class, Bird '''
    _height = 34
    _width = 24
    _flapAccel = -9
    _velY = -9
    _maxVelY = 10
    _minVelY = -8
    _accelY = 1
    _rotation = 45
    _flapped = False

    image = 'assets/sprites/redbird-midflap.png'
    posx = 0
    posy = 0
    index = 0
    shmvals = {}

    def __init__(self):
        posx = int(SCREENWIDTH*.02)
        posy = int((SCREENHEIGHT - self._height) / 2)
        index = 0
        shmvals = {'val': 2, 'dir': 1}

    def set_pos(self, x,y):
        self.posx = x
        self.posy = y

    def move_foward(self):
        self.set_pos(self.posx-1, self.posy)
        self.get_pos()

    def get_pos(self):
        print (self.posx, self.posy)

    def bounds_check(self):
        if self.posy + self._height >= BASEY -1:
            return [True, True]




class FlappyGame:
    player = Bird()
    gameheight = SCREENHEIGHT
    gamewidth = SCREENWIDTH
    base_y = SCREENHEIGHT * 0.79
    pipes = []

    def getrandomPipe(self):
        gapY = random.randrange(0, int(BASEY * 0.6 - PIPEGAPSIZE))
        gapY += int(BASEY * 0.2)
        pipeX = SCREENWIDTH + 10
        self.pipes.append(
            [{'x': pipeX, 'y': gapY - pipe_height},  #  upper
             {'x': pipeX, 'y': gapY + PIPEGAPSIZE}] #  lower
        )
        return self.pipes[self.pipes.__len__()-1]

    def getPipe(self):
        return self.pipes[self.pipes.__len__()-1]


    def checkCrash(self):
        self.player.bounds_check()
        if self.player.posy


    def initializeGame(self):
        basex = 80
        baseShift = base_width - backg_width

    def runGame(self):
        score = 0
        newPipe1 = self.getrandomPipe()
        newPipe2 = self.getrandomPipe()


        # list of upper pipes
        upperpipes = [
            {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
            {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
        ]
        # list of lowerpipe
        lowerpipes = [
            {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
            {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
        ]

        while True:
            if self.player.posy > -2 * bird_height:
                self.player._velY = self.player._flapAccel
                self.player._flapped = True









def main():
    game = FlappyGame()



if __name__ == '__main__':
    main()























