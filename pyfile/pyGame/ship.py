import pygame
class Ship():
    def __init__(self,screen,ai_settings):
        '''初始化飞船并设置其初始位置'''
        shipInmage_filename = r'D:\pythonCharm\Test\project_Game\alien_WarGame\pyfile\images\ship.bmp'
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(shipInmage_filename)                         # 加载图像
        self.rect = self.image.get_rect()                                           # get_rect()获取相应surface的属性rect
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx                                # centerx（飞船中心的x坐标）
        self.rect.bottom = self.screen_rect.bottom                                  # 要让游戏元素与屏幕边缘对齐，可使用属性top、bottom、left或right；
                                                                                    # 要调整游戏元素的水平或垂直位置，可使用属性x和y，它们分别是相应矩形左上角的x和y坐标
        self.center = float(self.rect.centerx)

        self.move_right = False
        self.move_left = False

    def blitme(self):                                                               # 不知怎么来的，屏幕中绘制和定位飞船
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:            # 判断飞船右位置与屏幕右位置
            self.center += self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.left > 0:                                   # 0也可以用self.screen_rect.left代替
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center                                             # 将self.center的值同步给self.rect.centerx，从而改变飞船的位置


