import pygame

class SpriteSheet:

    def __init__(self, filename, size, dims):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
            self.sheet = pygame.transform.scale(self.sheet, ( size[0]*dims[0], size[1]*dims[1] ))
            self.size = size
            self.dims = dims
            self.rect = pygame.Rect((0,0),size)
            self.images = self.load_strip(self.rect, dims)
            print('images loaded {}'.format(len(self.images)))
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        colorkey = image.get_at((5,5))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, dims):
        """Load a whole strip of images, and return them as a list."""
        rects = []
        colorkey = None
        x, y = dims
        for j in range(y):
          for i in range(x):
            rects.append(pygame.Rect(rect[0]+rect[2]*i, rect[1]+rect[3]*j, rect[2], rect[3]))
        return self.images_at(rects, colorkey)