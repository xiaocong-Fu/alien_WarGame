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

    def update(self):
        '''向右或向左移动外星人'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''
        screen_rect  =self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True


