import pygame
from settings import *


class Level:
    def __init__(self):
        # get the display surface
        # 得到的结果和main中，Game.screen 显示界面是同一个
        self.display_surface = pygame.display.get_surface()

        # sprite groups角色组
        self.all_sprites = pygame.sprite.Group()

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()
