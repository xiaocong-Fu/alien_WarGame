import game_functions as gf
import pygame
from settings import Settings
from ship import Ship


def run_game():
    '''初始化游戏并创建对象'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))                  # pygame.display.set_mode()：来创建一个名为screen的显示窗口
    pygame.display.set_caption("Alien Invasion")
    # bg_color = ai_settings.bg_color

    ship = Ship(screen,ai_settings)                                                         # 创建一艘飞船
    '''开始游戏主循环'''
    while True:
        # for event in pygame.event.get():                                        # pygame.event.get():访问Pygame检测到的事件,键盘鼠标事件
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship)
        ship.update()
        # screen.fill(bg_color)                                                   # 每次循环时都重绘屏幕，screen.fill()：用背景色填充屏幕
        # ship.blitme()
        # pygame.display.flip()
        gf.update_screen(ai_settings,screen,ship)

run_game()