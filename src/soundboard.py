# Place sounds in sounds folder in sound_ij.wav format
# being i row number and j column number (starting at 0)

import pygame

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

# init fonts
fontLogo = pygame.font.Font('res/Kathen.otf', int(spacing/1.5))
fontObj = pygame.font.Font('res/Hyperspace.otf', int(spacing/2.5))

# init the soundboard data (list of dictionaries)
data = []

# generate sound button objects
for i in range(rows):
    for j in range(rows):
        data.append({
            'column': i,
            'row': j,
            'text': 'empty',
            'path': 'sounds/fallback.wav',
            'soundobj': pygame.mixer.Sound('sounds/fallback.wav'),
            'coord': (spacing*(2*i+1), spacing*(2*j+1)),
            'size': (spacing, spacing),
            'rectobj': pygame.Rect(spacing*(2*i+1), spacing*(2*j+1), spacing, spacing),
            'textobj': fontObj.render(str(i)+str(j), False, (0, 0, 0)),
            'textcoords': (spacing*(2*i+1.5), spacing*(2*j+1.5)),
            'color': (150, 150, 150),
            'bordecolor': (255, 255, 0),
            'borderzise': (spacing+12, spacing+12),
            'loop': False
        })

# draw logo
logo = fontLogo.render('pySoundboard', True, (55, 55, 55))
logoRect = logo.get_rect()
logoRect.midright = (spacing*(2*rows), size[1]-spacing/2)

# initialize clock. used later in the loop.
clock = pygame.time.Clock()

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
    x, y = pygame.mouse.get_pos()
    for elem in data:
        if elem['rectobj'].collidepoint(x, y):
            elem['soundobj'].play()
            pygame.draw.rect(screen, (255, 255, 0), [
                             elem['coord'][0]-6, elem['coord'][1]-6, spacing+12, spacing+12], 1)
    # write draw code here
    screen.blit(logo, logoRect)
    for elem in data:
        pygame.draw.rect(screen, elem['color'], elem['rectobj'])
        screen.blit(elem['textobj'], elem['textcoords'])

    # display what’s drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)

# close the window and quit
pygame.quit()
