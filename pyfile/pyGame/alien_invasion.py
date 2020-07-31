import game_functions as gf
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    '''初始化游戏并创建对象'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))                  # pygame.display.set_mode()：来创建一个名为screen的显示窗口
    pygame.display.set_caption("Alien Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings,screen,'Play')

    # bg_color = ai_settings.bg_color

    ship = Ship(screen,ai_settings)                                                         # 创建一艘飞船
    # alien = Alien(ai_settings,screen)
    stats = GameStats(ai_settings)
    bullets = Group()                                                                       # 创建一个用于存储子弹的编组
    aliens = Group()                                                                        # 创建一个用于存储外星人的编组
    gf.create_fleet(ai_settings,screen,aliens,ship)
    '''开始游戏主循环'''
    while True:
        # for event in pygame.event.get():                                        # pygame.event.get():访问Pygame检测到的事件,键盘鼠标事件
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship,ai_settings,screen,bullets,stats,play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets,aliens,ai_settings,screen,ship)
            gf.update_aliens(aliens,ai_settings,ship,stats,screen,bullets)

        gf.update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats)

run_game()