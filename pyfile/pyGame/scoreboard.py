import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    '''显示得分信息的类'''
    def __init__(self,ai_settings,screen,stats):
        '''初始化显示得分涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.high_text_color = (255,0,0)
        self.level_color = (255,128,0)
        self.font = pygame.font.SysFont(None,55)

        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分转化为一副渲染的图像'''
        rounded_score = int(round(self.stats.score,-1))                                                                     # round():让小数精确到小数点后几位,-1:标识取整。
        score_str = "Score: " + "{:,}".format(rounded_score)                                                                # 使用了一个字符串格式设置指令，
                                                                                                                            # 它让Python将数值转换为字符串时在其中插入逗号
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 60

    def prep_high_score(self):
        '''将最高分转换为渲染图像'''
        high_score = int(round(self.stats.high_score))
        high_score_str = "Total Score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.high_text_color, self.ai_settings.bg_color)
        # 将最高分放在屏幕左上角
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 10

    def prep_level(self):
        '''将等级转换为渲染图像'''
        level = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level, True, self.level_color, self.ai_settings.bg_color)
        # 将最高分放在屏幕左上角
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.bottom = self.screen_rect.bottom - 10

    def prep_ships(self):
        '''显示还余下几艘飞船'''
        self.ships = Group()                                                                    # 创建一个空编组self.ships
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen,self.ai_settings)
            ship.rect.x = 15 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)                                                                # 将每艘飞船添加进ships中


    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)

