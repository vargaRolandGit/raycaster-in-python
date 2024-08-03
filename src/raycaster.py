from src.conf import *
from src.player import Player

import pygame
import sys

class RayCaster:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player()

    def draw_map(self):
        for row in range(MAP_SIZE):
            for column in range(MAP_SIZE):
                square = row * MAP_SIZE + column

                pygame.draw.rect(
                    self.window, 
                    (200, 200, 200) if MAP[square] == '#' else (100,100,100), 
                    (column * TILE_SIZE, 
                    row * TILE_SIZE, 
                    TILE_SIZE,
                    TILE_SIZE )
                )

        self.player.draw(self.window)

    def cast_rays(self):
        start_angle = self.player.angle - HALF_FOV

        for ray in range(CASTED_RAYS):
            for dept in range(MAX_DEPTH):
                target_x = self.player.x - math.sin(start_angle) * dept
                target_y = self.player.y + math.cos(start_angle) * dept

                square = int(target_y / TILE_SIZE) * MAP_SIZE + int(target_x / TILE_SIZE)

                if MAP[square]== '#':
                    pygame.draw.rect(
                        self.window, 'green',
                        (
                            int(target_x / TILE_SIZE) * TILE_SIZE, 
                            int(target_y / TILE_SIZE) * TILE_SIZE,
                            TILE_SIZE - 2,
                            TILE_SIZE - 2
                        )
                    )

                    wall_height = 21000 / (dept + 0.0001)
                    color = 255 - int(dept * 200) / 255 
                    pygame.draw.rect(self.window, (color, color, color), (
                        ray * SCALE,
                        ((WINDOW_HEIGHT / 2) - wall_height / 2),
                        SCALE, wall_height
                    ))

                    break

                pygame.draw.line(
                    self.window, 'yellow',
                    (self.player.x, self.player.y),
                    (target_x, target_y),
                    1  
                )

            start_angle += STEP_ANGLE


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            self.window.fill('black')

            pygame.draw.rect(
                self.window, (150,150,150), 
                (
                    0, 0, WINDOW_WIDTH, WINDOW_HEIGHT / 2
                )
            )
            pygame.draw.rect(
                self.window, (50,50,50), 
                (
                    0, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT
                )
            )

            self.cast_rays()
            self.draw_map()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: self.player.angle  -= .1
            if keys[pygame.K_RIGHT]: self.player.angle += .1

            if keys[pygame.K_UP]:
                self.player.x += -math.sin(self.player.angle)
                self.player.y += math.cos(self.player.angle)
            elif keys[pygame.K_DOWN]:
                self.player.x -= -math.sin(self.player.angle)
                self.player.y -= math.cos(self.player.angle)


            pygame.display.flip()
            self.clock.tick(FPS)