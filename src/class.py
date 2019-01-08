# WIP


class button:
    'A class for the soundboard button'

    def __init__(self, sound='', coords=(0, 0), size=(50, 50), text='empty', color=(0, 0, 0), bordercolor=(0, 0, 0), volume=6, loop=False, isplaying=False):
        self.sound = pygame.mixer.Sound(sound)
        self.coords = coords
        self.size = size
        self.text = text
        self.color = color
        self.bordercolor = bordercolor
        self.volume = volume
        self.loop = loop
        self.isplaying = isplaying

    def getrect(self):
        return

    def setsound(self, sound):
        return pygame.mixer.Sound(self.sound)

    def setloop(self, loop):
        self.loop = loop

    def play(self):
        pass

    def length(self):
        pass

    def fadeout(self):
        pass

    def stop(self):
        pass

    def setvolume(self, volume):
        self.volume = volume

    def __str__(self):
        return f'Button with coordinates {self.coords} and text {self.text} associated to sound {self.sound} and loop set to {self.loop}'


button1 = button()

print(button1)

button1.setloop = True
