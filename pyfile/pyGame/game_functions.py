import sys
import pygame
from pyGame.bullet import Bullet

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    '''响应按键'''
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:                                             # 按下右键向右移动
        ship.move_right = True
    if event.key == pygame.K_LEFT:                                              # 按下左键
        ship.move_left = True
    if event.key == pygame.K_UP:
        ship.move_up =True
    if event.key == pygame.K_DOWN:
        ship.move_down = True
    if event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)

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


def check_events(ship,ai_settings,screen,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:                                    # pygame.KEYDOWN,键按下,pygame.KEYUP，键抬起,标识按键事件的行为状态。
            check_keydown_events(event,ship,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)



def update_screen(ai_settings,screen,ship,bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():                                           # 绘制所有子弹
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    '''更新子弹的位置，并删除已消失的子弹'''
    bullets.update()
    for bullet in bullets.copy():                                              # 删除已消失的子弹      copy()方法不知
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings,screen,ship,bullets):
    '''发射子弹'''
    if len(bullets) < ai_settings.bullets_allowed:                              # 限制屏幕中子弹数量
        new_bullet = Bullet(ai_settings, screen, ship)                          # 创建子弹，并将其加入到编组bullets中
        bullets.add(new_bullet)
        print(len(bullets))
