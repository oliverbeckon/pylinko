from ball import Ball
from board import *
from multis import *
from settings import *
import ctypes, pygame, pymunk, random, sys
from playerAtr import *

# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        playerInit()
        pygame.display.set_caption(TITLE_STRING)
        self.clock = pygame.time.Clock()
        self.delta_time = 0

        # Pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0, 2000)

        # Plinko setup
        self.ball_group = pygame.sprite.Group()
        self.board = Board(self.space)

        # Debugging
        self.balls_played = 0

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_c:
                            if getBallValue() < 200:
                                setBallValue(getBallValue() + 5)
                        case pygame.K_v:
                            if getBallValue() > 5:
                                setBallValue(getBallValue() - 5)
                        case pygame.K_SPACE:
                            if getMoney() >= getBallValue():
                                random_x = WIDTH//2 + random.choice([random.randint(-20, -1), random.randint(1, 20)])
                                click.play()
                                self.ball = Ball((random_x, 20), self.space, self.board, self.delta_time, getBallValue())
                                self.ball_group.add(self.ball)
                        case pygame.K_b:
                            self.ammount = round(getMoney() / getBallValue())
                            click.play()
                            for i in range(self.ammount):
                                random_x = WIDTH//2 + random.choice([random.randint(-20, -1), random.randint(1, 20)])
                                self.ball = Ball((random_x, 20), self.space, self.board, self.delta_time, getBallValue())
                                self.ball_group.add(self.ball)

                    


            self.screen.fill(BG_COLOR)

            # Time variables
            self.delta_time = self.clock.tick(FPS) / 1000.0

            # Pymunk
            self.space.step(self.delta_time)
            self.board.update()
            self.ball_group.update()

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()