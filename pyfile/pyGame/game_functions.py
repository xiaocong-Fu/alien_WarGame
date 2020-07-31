import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep                                                          # 函数sleep()，以便使用它来让游戏暂停

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    '''响应按键'''
    if event.key == pygame.K_ESCAPE:                                            # pygame.event.get():访问Pygame检测到的事件,键盘鼠标事件
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


def check_events(ship,ai_settings,screen,bullets,stats,play_button,aliens):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:                                    # pygame.KEYDOWN,键按下,pygame.KEYUP，键抬起,标识按键事件的行为状态。
            check_keydown_events(event,ship,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:                              # pygame.MOUSEBUTTONDOWN：鼠标点击按钮事件。
            mouse_x,mouse_y = pygame.mouse.get_pos()                            # pygame.mouse.get_pos()，它返回一个元组，其中包含玩家单击时鼠标的x和y坐标。
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_settings,screen,ship)


def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_settings,screen,ship):
    '''在玩家单击Play按钮时开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)              # collidepoint()检查鼠标单击位置是否在Play按钮的rect内。
    if button_clicked and not stats.game_active:
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        pygame.mouse.set_visible(False)                                          # 隐藏光标：set_visible()传递False，让Pygame在光标位于游戏窗口内时将其隐藏起来。
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建新的外星人并让飞船居中
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()



def update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():                                           # 绘制所有子弹
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 若游戏非活跃状态,就绘制Play按钮
    if not stats.game_active:                                                   # 为让Play按钮显示在所有元素之上，绘制完其他元素后，最后在绘制Play按钮
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(bullets,aliens,ai_settings,screen,ship):
    '''更新子弹的位置，并删除已消失的子弹'''
    bullets.update()
    for bullet in bullets.copy():                                              # 删除已消失的子弹      copy()方法不知
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(bullets,aliens,ai_settings,screen,ship)


def check_bullet_alien_collisions(bullets,aliens,ai_settings,screen,ship):
    '''响应子弹和外星人的碰撞'''
    # 检测子弹是否碰撞到外星人,若碰到就删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True,True)         # sprite.groupcollide()将每颗子弹的rect同每个外星人的rect进行比较,
                                                                                # 并返回一个字典，其中包含发生了碰撞的子弹和外星人。
                                                                                # 在这个字典中，每个键都是一颗子弹，而相应的值都是被击中的外星人.
    # 外星人组为空则创建一批新的外星人
    if len(aliens) == 0:
        bullets.empty()  # empty()删除编组中余下的所有精灵，从而删除现有的所有子弹
        create_fleet(ai_settings, screen, aliens, ship)


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


def ship_hit(ai_settings,stats,ship,screen,alines,bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left > 0:
        # 将ship_left  -1
        stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        alines.empty()
        bullets.empty()
        # 创建新的外星人，并将飞船放置到原位
        create_fleet(ai_settings,screen,alines,ship)
        ship.center_ship()
        # 暂停
        sleep(1)
    else:
        stats.game_active = False
        # 游戏结束显示光标
        pygame.mouse.set_visible(True)


def check_alien_bottom(screen,aliens,ai_settings,stats,ship,bullets):
    '''检查是否有外星人到达屏幕底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom > screen_rect.bottom:
            ship_hit(ai_settings,stats,ship,screen,aliens,bullets)
            break


def update_aliens(aliens,ai_settings,ship,stats,screen,bullets):
    '''更新外星人中所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):                                 # spritecollideany()接受两个实参：一个精灵和一个编组。
                                                                                    # 它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生了碰撞的成员后就停止遍历编组
        ship_hit(ai_settings,stats,ship,screen,aliens,bullets)
    # 检查是否有外星人到达屏幕底部
    check_alien_bottom(screen,aliens,ai_settings,stats,ship,bullets)


