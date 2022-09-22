import pygame
from settings import *


# 基本角色
class Player(pygame.sprite.Sprite):  # 继承自精灵类
    def __init__(self, pos, group):
        super().__init__(group)  # 只要创建一个 Player 实例，就会存在 group 这个组里面

        # general setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        # pygame 坐标系原点默认在窗口左上角
        self.rect = self.image.get_rect(center=pos)

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

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


# 角色B. 自由发挥
class PlayerB(pygame.sprite.Sprite):  # 继承自精灵类
    def __init__(self, pos, group):
        super().__init__(group)  # 只要创建一个 Player 实例，就会存在 group 这个组里面

        # general setup
        self.image = pygame.Surface((21, 42))
        self.image.fill('skyblue')
        self.rect = self.image.get_rect(center=pos)

        # movement attributes   移动属性
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    # 根据输入计算移动的方向向量
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, dt):

        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement 水平移动
        self.pos.x += self.direction.x * self.speed * dt
        if self.pos.x >= SCREEN_WIDTH:
            self.pos.x = SCREEN_WIDTH
        elif self.pos.x <= 0:
            self.pos.x = 0
        self.rect.centerx = self.pos.x

        # vertical movement 垂直移动
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
