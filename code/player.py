import pygame
from settings import *
from support import *


# 基本角色
class Player(pygame.sprite.Sprite):  # 继承自精灵类
    def __init__(self, pos, group):
        super().__init__(group)  # 只要创建一个 Player 实例，就会存在 group 这个组里面

        # 美术资源
        self.import_assets()
        self.status = 'left_water'
        self.frame_index = 0 # 帧

        # general setup
        # 显示属性
        self.image = self.animations[self.status][self.frame_index]
        # pygame 坐标系原点默认在窗口左上角
        self.rect = self.image.get_rect(center=pos)

        # movement attributes 运动属性
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    # 加载角色立绘
    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
                           'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
                           'right_water': [], 'left_water': [], 'up_water': [], 'down_water': [],
                           }
        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation]=import_forder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, dt):

        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement 水平移动
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement 垂直移动
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
