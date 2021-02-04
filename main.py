#
# Moh's Checkers game
# A simple checkers game made in Python using Pygame
# ... github link
# 
# Released under the GNU General Public License
try:
    import pygame
    import os, sys 
    from pygame.locals import *
    import random
except ImportError as err:
    print("Couldn't load module {}".format(err))
    sys.exit(2)

def load_img(name):
    """ Load image and return mage object """
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print("Cannot load image:", fullname)
        raise SystemExit(message)
    return image, image.get_rect()
    
test = load_img('red_piece.png')