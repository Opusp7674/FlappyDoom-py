import pygame
import sys
from bird import *
from pipes import *
from game_objects import *
from settings import *
from fire import *


class FlappyDoom:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.sound = Sound()
        self.score = Score(self)
        self.fire = DoomFire(self)
        self.new_game()

    def load_assets(self):
        # bird
        self.bird_images = [pygame.image.load(f'assets/bird/{i}.png').convert_alpha() for i in range(5)]
        bird_image = self.bird_images[0]
        bird_size = bird_image.get_width() * BIRD_SCALE, bird_image.get_height() * BIRD_SCALE
        self.bird_images = [pygame.transform.scale(sprite, bird_size) for sprite in self.bird_images]
        # background
        self.background_image = pygame.image.load('assets/images/bg.png').convert()
        self.background_image = pygame.transform.scale(self.background_image, RES)
        # ground
        self.ground_image = pygame.image.load('assets/images/ground.png').convert()
        self.ground_image = pygame.transform.scale(self.ground_image, (WIDTH, GROUND_HEIGHT))
        # pipes
        self.top_pipe_image = pygame.image.load('assets/images/top_pipe.png').convert_alpha()
        self.top_pipe_image = pygame.transform.scale(self.top_pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.bottom_pipe_image = pygame.transform.flip(self.top_pipe_image, False, True)
        # bird mask
        mask_image = pygame.image.load('assets/bird/mask.png').convert_alpha()
        mask_size = mask_image.get_width() * BIRD_SCALE, mask_image.get_height() * BIRD_SCALE
        self.mask_image = pygame.transform.scale(mask_image, mask_size)

    def new_game(self):
        self.all_sprites_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.bird = Bird(self)
        self.background = Background(self)
        self.ground = Ground(self)
        self.pipe_handler = PipeHandler(self)

    def draw(self):
        self.background.draw()
        self.fire.draw()
        self.all_sprites_group.draw(self.screen)
        self.ground.draw()
        self.score.draw()
        pygame.display.flip()

    def update(self):
        self.background.update()
        self.fire.update()
        self.all_sprites_group.update()
        self.ground.update()
        self.pipe_handler.update()
        self.clock.tick(FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.bird.check_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = FlappyDoom()
    game.run()