import pyGame.game_functions as gf
import pygame
from pyGame.settings import Settings
from pyGame.ship import Ship
from pygame.sprite import Group

def run_game():
    '''初始化游戏并创建对象'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))                  # pygame.display.set_mode()：来创建一个名为screen的显示窗口
    pygame.display.set_caption("Alien Invasion")
    # bg_color = ai_settings.bg_color

    ship = Ship(screen,ai_settings)                                                         # 创建一艘飞船
    bullets = Group()                                                                       # 创建一个用于存储子弹的编组
    '''开始游戏主循环'''
    while True:
        # for event in pygame.event.get():                                        # pygame.event.get():访问Pygame检测到的事件,键盘鼠标事件
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship,ai_settings,screen,bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():                                           # 删除已消失的子弹      copy()方法不知
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)


        # screen.fill(bg_color)                                                   # 每次循环时都重绘屏幕，screen.fill()：用背景色填充屏幕
        # ship.blitme()
        # pygame.display.flip()
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()