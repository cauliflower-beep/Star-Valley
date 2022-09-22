import pygame
from settings import *
from player import Player


# 关卡
class Level:
    def __init__(self):
        # get the display surface   画面展示
        # 得到的结果和main中，Game.screen 显示界面是同一个
        # self.player = None
        self.display_surface = pygame.display.get_surface()

        # sprite groups角色组管理
        self.all_sprites = pygame.sprite.Group()

        # 初始化角色
        self.setup()
    
    # 创建精灵实例    
    def setup(self):    
        self.player = Player((640,360),self.all_sprites)
        
    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
