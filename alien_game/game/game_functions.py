import sys
import pygame
from game import bullet


def check_events(ship, ai_settings, screen, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建子弹加入编组
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = bullet.Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    # 更新屏幕上的图像，并且换到新屏幕
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bt in bullets.sprites():
        bt.draw_bullet()

    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹位置
    bullets.update()
    # 删除消失的子弹
    for bt in bullets.copy():
        if bt.rect.bottom <= 0:
            bullets.remove(bt)
