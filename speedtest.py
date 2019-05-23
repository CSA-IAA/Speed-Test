'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
Movement, audio, clickability
Version 1.0
'''

import pygame, sys, random, itertools, time
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number of rows of icons
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
#set up the colors
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
#draw on the surface object

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY

DONUT = 'donut'
SQUARE = 'square'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, LINES, OVAL)

global sameshape
sameshape = []
global count
count = 0


def shapeandcolor():
    global FPSCLOCK, DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Speed Test')

    pygame.mixer.music.load('DarkKnight.mp3')  # imports the music
    pygame.mixer.music.play(-1, 0.0)  # duration of the music, in this case -1 means forever

    DISPLAYSURF.fill(BGCOLOR)


    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))
    random.shuffle(icons)  # randomize the order of the icons list
    global shape2,color2
    shape2, color2 = icons[0]
    xvalRec = random.randint(70, 560)
    yvalRec = random.randint(90, 400)
    xvalRec2 = random.randint(70, 560)
    yvalRec2 = random.randint(70, 400)
    widRec = random.randint(20, 120)
    heightRec = random.randint(20, 90)
    xval1Line = random.randint(70, 200)
    xval2Line = random.randint(200, 400)
    yval1Line = random.randint(90, 300)
    yval2Line = random.randint(301, 400)
    xval1Line2 = random.randint(70, 200)
    xval2Line2 = random.randint(200, 400)
    yval1Line2 = random.randint(70, 300)
    yval2Line2 = random.randint(301, 400)
    xvalCirc = random.randint(70, 580)
    yvalCirc = random.randint(90, 400)
    xvalCirc2 = random.randint(70, 560)
    yvalCirc2 = random.randint(70, 400)
    radiCirc = random.randint(15, 25)
    xvalElip = random.randint(70, 560)
    yvalElip = random.randint(90, 400)
    xvalElip2 = random.randint(70, 560)
    yvalElip2 = random.randint(70, 400)
    widthElip = random.randint(20, 100)
    heighElip = random.randint(20, 70)

    # Draw the shapes
    if shape2 == 'donut':
        pygame.draw.circle(DISPLAYSURF, color2, (30, 50), radiCirc)
        if 30 and 50 != xvalCirc2 and yvalCirc2:  # so shapes won't overlap
            pygame.draw.circle(DISPLAYSURF, color2, (xvalCirc2, yvalCirc2), radiCirc)
            shapestat = str(xvalCirc2), str(yvalCirc2), str(radiCirc)
            sameshape.append(('circle'))
            sameshape.append(shapestat)
        else:
            xvalCirc2 = random.randint(70, 560)
            yvalCirc2 = random.randint(70, 400)
            pygame.draw.circle(DISPLAYSURF, color2, (xvalCirc2, yvalCirc2), radiCirc)
            shapestat = str(xvalCirc2), str(yvalCirc2), str(radiCirc)
            sameshape.append(('circle'))
            sameshape.append(shapestat)

        ranlis = ['1', '2', '3']  # the one thats not a match
        block = random.choice(ranlis)
        if block == '1':
            pygame.draw.rect(DISPLAYSURF, color2, (xvalRec, yvalRec, widRec, heightRec))
            main()
        elif block == '2':
            pygame.draw.line(DISPLAYSURF, color2, (xval1Line, yval1Line), (xval2Line, yval2Line), 4)
            main()

        elif block == '3':
            pygame.draw.ellipse(DISPLAYSURF, color2, (xvalElip, yvalElip, widthElip, heighElip))
            main()


    elif shape2 == 'square':
        pygame.draw.rect(DISPLAYSURF, color2, (15, 50, widRec, heightRec))
        if 15 and 50 != xvalRec2 and yvalRec2:
            pygame.draw.rect(DISPLAYSURF, color2, (xvalRec2, yvalRec2, widRec, heightRec))
            shapestat = str(xvalRec2), str(yvalRec2), str(widRec), str(heightRec)
            sameshape.append(('rect'))
            sameshape.append(shapestat)
        else:
            xvalRec2 = random.randint(70, 560)
            yvalRec2 = random.randint(70, 400)
            pygame.draw.rect(DISPLAYSURF, color2, (xvalRec2, yvalRec2, widRec, heightRec))
            shapestat = str(xvalRec2), str(yvalRec2), str(widRec), str(heightRec)
            sameshape.append(('rect'))
            sameshape.append(shapestat)

        ranlis2 = ['1', '2', '3']
        block2 = random.choice(ranlis2)
        if block2 == '1':
            pygame.draw.circle(DISPLAYSURF, color2, (xvalCirc, yvalCirc), radiCirc)
            main()

        elif block2 == '2':
            pygame.draw.line(DISPLAYSURF, color2, (xval1Line, yval1Line), (xval2Line, yval2Line), 4)
            main()

        elif block2 == '3':
            pygame.draw.ellipse(DISPLAYSURF, color2, (xvalElip, yvalElip, widthElip, heighElip))
            main()


    elif shape2 == 'lines':
        pygame.draw.line(DISPLAYSURF, color2, (15, 50), (100, 130), 4)
        if 15 and 100 and 50 and 130 != xval1Line2 and xval2Line2 and yval1Line2 and yval2Line2:
            pygame.draw.line(DISPLAYSURF, color2, (xval1Line2, yval1Line2), (xval2Line2, yval2Line2), 4)
            linet = 4
            shapestat = str(xval1Line2), str(yval1Line2), str(xval2Line2), str(yval2Line2), str(linet)
            sameshape.append(('line'))
            sameshape.append(shapestat)

        else:
            xval1Line2 = random.randint(70, 200)
            xval2Line2 = random.randint(200, 400)
            yval1Line2 = random.randint(70, 300)
            yval2Line2 = random.randint(301, 400)
            pygame.draw.line(DISPLAYSURF, color2, (xval1Line2, yval1Line2), (xval2Line2, yval2Line2), 4)
            linet = 4
            shapestat = str(xval1Line2), str(yval1Line2), str(xval2Line2), str(yval2Line2), str(linet)
            sameshape.append(('line'))
            sameshape.append(shapestat)

        ranlis4 = ['1', '2', '3']
        block4 = random.choice(ranlis4)
        if block4 == '1':
            pygame.draw.circle(DISPLAYSURF, color2, (xvalCirc, yvalCirc), radiCirc)
            main()

        elif block4 == '2':
            pygame.draw.rect(DISPLAYSURF, color2, (xvalRec, yvalRec, widRec, heightRec))
            main()

        elif block4 == '3':
            pygame.draw.ellipse(DISPLAYSURF, color2, (xvalElip, yvalElip, widthElip, heighElip))
            main()


    elif shape2 == 'oval':
        pygame.draw.ellipse(DISPLAYSURF, color2, (20, 50, widthElip, heighElip))
        if 20 and 50 != xvalElip2 and yvalElip2:
            pygame.draw.ellipse(DISPLAYSURF, color2, (xvalElip2, yvalElip2, widthElip, heighElip))
            shapestat = str(xvalElip2), str(yvalElip2), str(widthElip), str(heighElip)
            sameshape.append(('ellipse'))
            sameshape.append(shapestat)
        else:
            xvalElip2 = random.randint(70, 560)
            yvalElip2 = random.randint(70, 400)
            pygame.draw.ellipse(DISPLAYSURF, color2, (xvalElip2, yvalElip2, widthElip, heighElip))
            shapestat = str(xvalElip2), str(yvalElip2), str(widthElip), str(heighElip)
            sameshape.append(('ellipse'))
            sameshape.append(shapestat)

        ranlis5 = ['1', '2', '3']
        block5 = random.choice(ranlis5)
        if block5 == '1':
            pygame.draw.circle(DISPLAYSURF, color2, (xvalCirc, yvalCirc), radiCirc)
            main()

        elif block5 == '2':
            pygame.draw.rect(DISPLAYSURF, color2, (xvalRec, yvalRec, widRec, heightRec))
            main()

        elif block5 == '3':
            pygame.draw.line(DISPLAYSURF, color2, (xval1Line, yval1Line), (xval2Line, yval2Line), 4)
            main()



def  main():
    global sameshape
    global shape2, color2
    done = False
    global count
    basicfont = pygame.font.SysFont(None, 48)  # 48 is font size, no font type
    text = basicfont.render(str(count), True, BLACK, BGCOLOR)  # first set of parenthesis is the font color, second set is the background of the words
    DISPLAYSURF.blit(text, (500, 0))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    secondval = []
                    for x in sameshape[1]:
                        secondval.append(x)
                    if sameshape[0] == 'circle':
                        clickity = pygame.draw.circle(DISPLAYSURF, color2,(int(secondval[0]), int(secondval[1])), int(secondval[2]))
                        if clickity.collidepoint(event.pos):
                            DISPLAYSURF.fill(NAVYBLUE)
                            pygame.display.flip()
                            count += 1
                            text = basicfont.render(str(count), True, BLACK, BGCOLOR)  # first set of parenthesis is the font color, second set is the background of the words
                            DISPLAYSURF.blit(text, (500, 0))
                            soundObj = pygame.mixer.Sound('cheer.wav')  # imports the music on standby
                            soundObj.play()
                            del sameshape[:] #gets rid of prev shape values
                            shapeandcolor()
                        else:
                            soundObj2 = pygame.mixer.Sound('SHUTDOWN.wav')  # imports the music on standby
                            soundObj2.play()
                            pygame.time.wait(2000)
                            pygame.quit()
                            sys.exit()


                    elif sameshape[0] == 'rect':
                        clickity = pygame.draw.rect(DISPLAYSURF, color2,(int(secondval[0]), int(secondval[1]), int(secondval[2]), int(secondval[3])))
                        if clickity.collidepoint(event.pos):
                            DISPLAYSURF.fill(NAVYBLUE)
                            pygame.display.flip()
                            count += 1
                            text = basicfont.render(str(count), True, BLACK, BGCOLOR)  # first set of parenthesis is the font color, second set is the background of the words
                            DISPLAYSURF.blit(text, (500, 0))
                            soundObj = pygame.mixer.Sound('cheer.wav')  # imports the music on standby
                            soundObj.play()
                            del sameshape[:]  # gets rid of prev shape values
                            shapeandcolor()
                        else:
                            soundObj2 = pygame.mixer.Sound('SHUTDOWN.wav')  # imports the music on standby
                            soundObj2.play()
                            pygame.time.wait(2000)
                            pygame.quit()
                            sys.exit()


                    elif sameshape[0] == 'line':
                        clickity = pygame.draw.line(DISPLAYSURF, color2,(int(secondval[0]), int(secondval[1])), (int(secondval[2]), int(secondval[3])), int(secondval[4]))
                        if clickity.collidepoint(event.pos):
                            DISPLAYSURF.fill(NAVYBLUE)
                            pygame.display.flip()
                            count += 1
                            text = basicfont.render(str(count), True, BLACK, BGCOLOR)  # first set of parenthesis is the font color, second set is the background of the words
                            DISPLAYSURF.blit(text, (500, 0))
                            soundObj = pygame.mixer.Sound('cheer.wav')  # imports the music on standby
                            soundObj.play()
                            del sameshape[:]  # gets rid of prev shape values
                            shapeandcolor()
                        else:
                            soundObj2 = pygame.mixer.Sound('SHUTDOWN.wav')  # imports the music on standby
                            soundObj2.play()
                            pygame.time.wait(2000)
                            pygame.quit()
                            sys.exit()


                    elif sameshape[0] == 'ellipse':
                        clickity = pygame.draw.ellipse(DISPLAYSURF, color2,(int(secondval[0]), int(secondval[1]), int(secondval[2]), int(secondval[3])))
                        if clickity.collidepoint(event.pos):
                            DISPLAYSURF.fill(NAVYBLUE)
                            pygame.display.flip()
                            count += 1
                            text = basicfont.render(str(count), True, BLACK, BGCOLOR)  # first set of parenthesis is the font color, second set is the background of the words
                            DISPLAYSURF.blit(text, (500, 0))
                            soundObj = pygame.mixer.Sound('cheer.wav')  # imports the music on standby
                            soundObj.play()
                            del sameshape[:]  # gets rid of prev shape values
                            shapeandcolor()
                        else:
                            soundObj2 = pygame.mixer.Sound('SHUTDOWN.wav')  # imports the music on standby
                            soundObj2.play()
                            pygame.time.wait(2000)
                            pygame.quit()
                            sys.exit()


        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    pygame.init()
    shapeandcolor()
    pygame.quit()
    sys.exit()
    pygame.mixer.music.stop()
    soundObj.stop()
    soundObj2.stop()