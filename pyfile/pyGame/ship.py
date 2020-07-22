import pygame
class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置其初始位置'''
        shipInmage_filename = r'D:/PyCharm/PyTest/alien_WarGame/alien_WarGame/pyfile/images/ship.bmp'
        self.screen = screen
        self.image = pygame.image.load(shipInmage_filename)                         # 加载图像
        self.rect = self.image.get_rect()                                           # get_rect()获取相应surface的属性rect
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx                                # centerx（飞船中心的x坐标）
        self.rect.bottom = self.screen_rect.bottom                                  # 要让游戏元素与屏幕边缘对齐，可使用属性top、bottom、left或right；
                                                                                    # 要调整游戏元素的水平或垂直位置，可使用属性x和y，它们分别是相应矩形左上角的x和y坐标


    def blitme(self):                                                               # 不知怎么来的
        self.screen.blit(self.image,self.rect)


