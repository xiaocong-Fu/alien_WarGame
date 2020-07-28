import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''单个外星人的类'''
    def __init__(self,ai_settings,screen):
        alienImage_filename = r'D:\pythonCharm\Test\project_Game\alien_WarGame\pyfile\images\alien.bmp'
        '''初始化外星人并设置位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(alienImage_filename)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        '''绘制外星人'''
        self.screen.blit(self.image,self.rect)
