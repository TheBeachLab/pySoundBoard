# Place sounds in sounds folder in sound_ij.wav format
# being i row number and j column number (starting at 0)

import pygame

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [800, 800]
screen = pygame.display.set_mode(size)  # , pygame.NOFRAME
pygame.display.set_caption('pySoundBoard')
# variables
rows = 4  # 10 max
spacing = int(size[0]/(1+2*rows))
# generate sound objects
for i in range(rows):
    for j in range(rows):
        try:
            exec(
                f'sound_{i}{j} = pygame.mixer.Sound("sounds/sound_{i}{j}.wav")')
        except:
            exec(f'sound_{i}{j} = pygame.mixer.Sound("sounds/fallback.wav")')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# create rectangles
for i in range(rows):
    for j in range(rows):
        exec(
            f'rect_{i}{j} = pygame.Rect(spacing*(2*{i}+1), spacing*(2*{j}+1), spacing, spacing)')


# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # write game logic here
    x, y = pygame.mouse.get_pos()
    for i in range(rows):
        for j in range(rows):
            exec(f'if rect_{i}{j}.collidepoint(x, y):sound_{i}{j}.play()')
    # clear the screen before drawing
    screen.fill((30, 30, 30))
    # write draw code here
    for i in range(rows):
        for j in range(rows):
            exec(f'pygame.draw.rect(screen, (150, 150, 150), rect_{i}{j})')
    # display what’s drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)

# close the window and quit
pygame.quit()
