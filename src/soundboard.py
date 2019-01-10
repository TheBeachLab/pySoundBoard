# Place sounds in sounds folder in sound_ij.wav format
# being i row number and j column number (starting at 0)

import pygame
import json

# variables
size = [800, 800]
rows = 4  # 10 max
spacing = int(size[0]/(1+2*rows))
print(spacing)

# initialize game engine
pygame.mixer.pre_init(44100, -16, 1, 512)  # fixes delay in play
pygame.init()
# set screen width/height and caption
screen = pygame.display.set_mode(size)  # , pygame.NOFRAME
pygame.display.set_caption('pySoundBoard')

data = {}  # init the soundboard data
data['buttons'] = []

# generate sound button objects
for i in range(rows):
    for j in range(rows):
        data['buttons'].append({
            'row': i,
            'column': j,
            'number': i+j,
            'text': 'empty',
            'sound': 'sounds/fallback.wav',
            'coord': (spacing*(2*i+1), spacing*(2*j+1)),
            'size': (spacing, spacing),
            'color': (150, 150, 150),
            'bordecolor': (255, 255, 0),
            'borderzise': (spacing+12, spacing+12),
            'loop': False
        })

# save JSON file
json.dump(data, open('data.json', 'w'))

# logo
fontLogo = pygame.font.Font('res/Kathen.otf', int(spacing/1.5))
logo = fontLogo.render('pySoundboard', True, (55, 55, 55))
logoRect = logo.get_rect()
logoRect.midright = (spacing*(2*rows), size[1]-spacing/2)

# button texts
# numbers = {}
# fontObj = pygame.font.Font('res/Hyperspace.otf', int(spacing/2.5))
# for i in range(rows**2):
#     textObj_{i}{j} = fontObj.render(str({i})+str({j}), False, (0, 0, 0))
#     # get the surrounding rectangle
#     textRectObj_{i}{j} = textObj_{i}{j}.get_rect()
#     # set the center of the rectangle
#     textRectObj_{i}{j}.center = (spacing*(2*{i}+1.5), spacing*(2*{j}+1.5))

# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# create rectangle
# for i in range(rows):
#     for j in range(rows):
#         pygame.Rect(spacing*(2*i+1), spacing*(2*j+1), spacing, spacing)

# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # clear the screen before drawing
    screen.fill((30, 30, 30))
    # write game logic here
    # x, y = pygame.mouse.get_pos()
    # for i in range(rows):
    #     for j in range(rows):
    #         exec(
    #             f'if rect_{i}{j}.collidepoint(x, y):sound_{i}{j}.play();pygame.draw.rect(screen, (255,255,0), [rect_{i}{j}.x-6, rect_{i}{j}.y-6, spacing+12, spacing+12], 1)')
    # write draw code here
    screen.blit(logo, logoRect)
    for i in range(rows):
        for j in range(rows):
            pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(
                spacing*(2*i+1), spacing*(2*j+1), spacing, spacing))
            # exec(f'screen.blit(textObj_{i}{j}, textRectObj_{i}{j})')

    # display what’s drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)

# close the window and quit
pygame.quit()
