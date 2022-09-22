import pygame
from settings import *
from support import *


# 基本角色
class Player(pygame.sprite.Sprite):  # 继承自精灵类
    def __init__(self, pos, group):
        super().__init__(group)  # 只要创建一个 Player 实例，就会存在 group 这个组里面

        # 美术资源
        self.import_assets()
        self.status = 'down_idle'   # 初始状态，角色静止
        self.frame_index = 0  # 帧

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
            self.animations[animation] = import_forder(full_path)

    # 动画效果 主要靠帧数实现
    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

        # 获取键盘等设备输入信号，转换相应状态

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    # 获取角色不同状态的立绘
    def get_status(self):
        # idle 角色静止时的立绘
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

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
        self.input()  # 获取输入
        self.get_status()  # 获取角色当前状态
        self.move(dt)
        self.animate(dt)
