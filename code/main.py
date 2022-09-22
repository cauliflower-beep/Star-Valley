import pygame, sys
from settings import *
from level import Level


# 游戏类
class Game:
    def __init__(self):
        # https://blog.csdn.net/qingtianZzzzz/article/details/84027873
        # init动作就是初始化所有模块，看看pygame是否可以正常为我们提供帮助
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Star Valley')
        self.clock = pygame.time.Clock()
        # 为了保持主函数尽可能简洁，这里level单独做一个模块。
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
