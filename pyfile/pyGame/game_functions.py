import sys
import pygame
from pyGame.bullet import Bullet
from pyGame.alien import Alien

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



def update_screen(ai_settings,screen,ship,bullets,aliens):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():                                           # 绘制所有子弹
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
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
        # print(len(bullets))



def get_number_alien_x(ai_settings,alien_width):
    '''计算每行可容纳多少个外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可容纳多少卫星人'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人并把放在当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings,screen,aliens,ship):
    '''创建外星人群'''
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_alien_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_fleet_edges(ai_settings,aliens):
    '''外星人到达边缘时采取相应措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''整群外星人下移，并改变方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(aliens,ai_settings):
    '''更新外星人中所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

