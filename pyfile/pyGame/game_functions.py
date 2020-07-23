import sys
import pygame

def check_keydown_events(event,ship):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:                                             # 按下右键向右移动
        ship.move_right = True
    if event.key == pygame.K_LEFT:                                              # 按下左键
        ship.move_left = True
    if event.key == pygame.K_UP:
        ship.move_up =True
    if event.key == pygame.K_DOWN:
        ship.move_down = True

def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:                                            # pygame.K_RIGHT，pygame.K_LEFT，pygame.K_UP，pygame.K_DOWN，表示按键事件的行为种类。
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    if event.key == pygame.K_UP:
        ship.move_up =False
    if event.key == pygame.K_DOWN:
        ship.move_down = False


def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:                                    # pygame.KEYDOWN,键按下,pygame.KEYUP，键抬起,标识按键事件的行为状态。
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)



def update_screen(ai_settings,screen,ship):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()