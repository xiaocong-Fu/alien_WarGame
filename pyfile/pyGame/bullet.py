import pygame
from pygame.sprite import Sprite                                        # 通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。

class Bullet(Sprite):
    '''对飞船发射子弹管理的类'''
    def __init__(self,ai_settings,screen,ship):
        super(Bullet, self).__init__()                                  # 代码super(Bullet, self).__init__()使用了Python 2.7语法。这种语法也适用于Python3
                                                                        # 但你也可以将这行代码简写为super().__init__()。
        self.screen = screen
        # 在（0,0）处创建一个表示子弹的矩形，在设置正确位置
        # 子弹并非基于图像的，因此我们必须使用pygame.Rect()类从空白开始创建一个矩形。
        # 创建这个类的实例时，必须提供矩形左上角的x坐标和y坐标，还有矩形的宽度和高度。我们在(0, 0)处创建这个矩形，
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 储存用小数表示子弹的位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''更新子弹位置'''
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        '''屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)              # 函数draw.rect()使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分


