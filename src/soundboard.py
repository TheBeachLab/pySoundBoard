# Place sounds in sounds folder in sound_ij.wav format
# being i row number and j column number (starting at 0)

import pygame
from pygame.locals import *

# variables
size = [800, 800]
rows = 4  # 10 max
spacing = int(size[0]/(1+2*rows))

# initialize game engine
pygame.mixer.pre_init(44100, -16, 1, 512)  # fixes delay in play
pygame.init()

# set screen width/height and caption
screen = pygame.display.set_mode(size)  # , pygame.NOFRAME
pygame.display.set_caption('pySoundBoard')

# init fonts
fontLogo = pygame.font.Font('res/Kathen.otf', int(spacing/1.5))
fontObj = pygame.font.Font('res/Hyperspace.otf', int(spacing/2.5))


def readpaths():
    '''read rows**2 lines from paths.txt file
    and create a list of paths'''
    paths = []
    with open("paths.txt") as myfile:
        paths = [next(myfile) for x in range(rows**2)]
    # remove white space
    paths = [line.rstrip('\n') for line in paths]
    return paths


def makebuttons():
    '''generate sound button objects according to the number of
    rows'''
    data = []
    for i in range(rows):
        for j in range(rows):
            data.append({
                'column': i,
                'row': j,
                'text': 'empty',
                'soundobj': pygame.mixer.Sound(paths[i+j]),
                'coord': (spacing*(2*i+1), spacing*(2*j+1)),
                'size': (spacing, spacing),
                'rectobj': pygame.Rect(spacing*(2*i+1), spacing*(2*j+1), spacing, spacing),
                'textobj': fontObj.render(str(i)+str(j), False, (0, 0, 0)),
                'textcoords': (spacing*(2*i+1.5), spacing*(2*j+1.5)),
                'color': (150, 150, 150),
                'bordercolor': (255, 255, 0),
                'bordersize': (spacing+12, spacing+12),
                'loop': False
            })
    return data


def makelogo():
    # draw logo according to the size of the buttons
    logo = fontLogo.render('pySoundboard', True, (55, 55, 55))
    logoRect = logo.get_rect()
    logoRect.midright = (spacing*(2*rows), size[1]-spacing/2)
    return (logo, logoRect)


# make the initial set of objects
paths = readpaths()
data = makebuttons()
logo = makelogo()

# initialize clock. used later in the loop.
clock = pygame.time.Clock()

paused = False

# Loop until the user clicks close button
done = False
while done == False:
    # clear the screen before drawing
    screen.fill((30, 30, 30))
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
            if event.key == K_f:
                pygame.mixer.fadeout(3000)
            elif event.key == K_p:
                if paused == False:
                    pygame.mixer.pause()
                    paused = True
                else:
                    pygame.mixer.unpause()
                    paused = False
            elif event.key == K_s:
                pygame.mixer.stop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for elem in data:
                if elem['rectobj'].collidepoint(pos):
                    elem['soundobj'].play()
                    pygame.draw.rect(screen, (255, 100, 0), (elem['coord'][0]-6,
                                                             elem['coord'][1]-6, elem['bordersize'][0], elem['bordersize'][1]), 5)
    # write game logic here
    pos = pygame.mouse.get_pos()
    for elem in data:
        if elem['rectobj'].collidepoint(pos):
            pygame.draw.rect(screen, elem['bordercolor'], (elem['coord'][0]-6,
                                                           elem['coord'][1]-6, elem['bordersize'][0], elem['bordersize'][1]), 1)
    # write draw code here
    screen.blit(logo[0], logo[1])
    for elem in data:
        pygame.draw.rect(screen, elem['color'], elem['rectobj'])
        screen.blit(elem['textobj'], elem['textcoords'])

    # display what’s drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)

# close the window and quit
pygame.quit()
