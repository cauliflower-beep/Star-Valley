import pygame
from settings import *
from player import Player,PlayerB


# 关卡
class Level:
    def __init__(self):
        # get the display surface
        # self.player = None
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    # 创建精灵实例
    def setup(self):
        self.player = Player((640, 360), self.all_sprites)  # 创建的精灵实例会放在 self.all_sprites 这个组中
        # 自由发挥：新增一个角色B
        self.playerB = PlayerB((320, 180), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt) # 会调用 self.all_sprites 中所有精灵的 update 方法
