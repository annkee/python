import pygame

from game import settings
from game import ship as sp
import game.game_functions as gf
from pygame.sprite import Group


def run_game():
    ai_settings = settings.Settings()
    # 初始化游戏，创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = sp.Ship(screen, ai_settings)

    # 创建存储子弹的编组
    bullets = Group()

    pygame.display.set_caption('Alien Invasion')

    # 开始游戏主循环
    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
