from multis import *
from obstacles import *
from settings import *
from playerAtr import getMoney
from ball import Ball
import pygame, pymunk

class Board():
    def __init__(self, space):
        self.space = space
        self.display_surface = pygame.display.get_surface()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 60)

        # Obstacles
        self.curr_row_count = 3
        self.final_row_count = 18
        self.obstacles_list = []
        self.obstacle_sprites = pygame.sprite.Group()
        self.updated_coords = OBSTACLE_START


        # Get second point for segmentA
        self.segmentA_2 = OBSTACLE_START
        while self.curr_row_count <= self.final_row_count:
            for i in range(self.curr_row_count):
                # Get first point for segmentB
                if self.curr_row_count == 3 and self.updated_coords[0] > OBSTACLE_START[0] + OBSTACLE_PAD:
                    self.segmentB_1 = self.updated_coords
                # Get first point for segmentA
                elif self.curr_row_count == self.final_row_count and i == 0:
                    self.segmentA_1 = self.updated_coords
                # Get second point for segmentB
                elif self.curr_row_count == self.final_row_count and i == self.curr_row_count - 1:
                    self.segmentB_2 = self.updated_coords
                self.obstacles_list.append(self.spawn_obstacle(self.updated_coords, self.space))
                self.updated_coords = (int(self.updated_coords[0] + OBSTACLE_PAD), self.updated_coords[1])
            self.updated_coords = (int(WIDTH - self.updated_coords[0] + (.5 * OBSTACLE_PAD)), int(self.updated_coords[1] + OBSTACLE_PAD))
            self.curr_row_count += 1
        self.multi_x, self.multi_y = self.updated_coords[0] + OBSTACLE_PAD, self.updated_coords[1]

        # Segments (boundaries on side of obstacles)
        self.spawn_segments(self.segmentA_1, self.segmentA_2, self.space)
        self.spawn_segments(self.segmentB_1, self.segmentB_2, self.space)
        # Segments at top of obstacles
        self.spawn_segments((self.segmentA_2[0], 0), self.segmentA_2, self.space)
        self.spawn_segments(self.segmentB_1, (self.segmentB_1[0], 0), self.space)

        # Spawn multis
        self.spawn_multis()

    def draw_obstacles(self, obstacles):
        for obstacle in obstacles:
            pos_x, pos_y = int(obstacle.body.position.x), int(obstacle.body.position.y)
            pygame.draw.circle(self.display_surface, (255, 255, 255), (pos_x, pos_y), OBSTACLE_RAD)

    # Used to give a border radius to previous multi display on right side
    def draw_prev_multi_mask(self):
        multi_mask_surface = pygame.Surface((WIDTH / 4, HEIGHT), pygame.SRCALPHA)
        multi_mask_surface.fill(BG_COLOR)
        right_side_of_board = (WIDTH / 16) * 13
        right_side_pad = right_side_of_board / 130
        mask_y = (HEIGHT / 4) + ((HEIGHT / 4) / 9)
        pygame.draw.rect(multi_mask_surface, (0, 0, 0, 0), (right_side_pad, mask_y, SCORE_RECT, SCORE_RECT * 4), border_radius=30)
        self.display_surface.blit(multi_mask_surface, (right_side_of_board, 0))

    def spawn_multis(self):
        self.multi_amounts = [val[1] for val in multi_rgb.keys()]
        self.rgb_vals = [val for val in multi_rgb.values()]
        for i in range(NUM_MULTIS):
            multi = Multi((self.multi_x, self.multi_y), self.rgb_vals[i], self.multi_amounts[i])
            multi_group.add(multi)
            self.multi_x += OBSTACLE_PAD

    def spawn_obstacle(self, pos, space):
        body = pymunk.Body(body_type = pymunk.Body.STATIC)
        body.position = pos
        body.friction = 0.6
        shape = pymunk.Circle(body, OBSTACLE_RAD)
        shape.elasticity = 0.4
        shape.filter = pymunk.ShapeFilter(categories=OBSTACLE_CATEGORY, mask=OBSTACLE_MASK)
        self.space.add(body, shape)
        obstacle = Obstacle(body.position.x, body.position.y)
        self.obstacle_sprites.add(obstacle)
        return shape

    def spawn_segments(self, pointA, pointB, space):
        segment_body = pymunk.Body(body_type = pymunk.Body.STATIC)
        segment_shape = pymunk.Segment(segment_body, pointA, pointB, 5) # radius = 5
        self.space.add(segment_body, segment_shape)


    def draw_text(self):
        self.money_surface = self.font.render(f'{getMoney()}$', False, (255,234,211))
        self.display_surface.blit(self.money_surface, (200, 50))


    def update(self):
        self.draw_obstacles(self.obstacles_list)
        multi_group.draw(self.display_surface)
        multi_group.update()
        if len(list(prev_multi_group)) > 0:
            prev_multi_group.update()
        if len(list(animation_group)) > 0:
            animation_group.update()
        self.draw_prev_multi_mask()
        self.draw_text()