import pygame
class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置其初始位置'''
        shipInmage_filename = r'D:/PyCharm/PyTest/alien_WarGame/alien_WarGame/pyfile/images/ship.bmp'
        self.screen = screen
        self.image = pygame.image.load(shipInmage_filename)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)


