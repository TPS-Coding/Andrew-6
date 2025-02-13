from settings import *
from random import choice, uniform


class Paddle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.Surface(SIZE["paddle"])
        self.image.fill(COLORS["paddle"])

        self.rect = self.image.get_frect(center=POS['player'])
        self.old_rect = self.rect.copy()
        
    def move(self, dt):
        self.rect.centery += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom
    
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.get_direction()
        self.move(dt) 


class Player(Paddle):
    def __init__(self, groups):
        super().__init__(groups)

        ## image and rect inherited from Paddle

        # movement
        self.speed = SPEED['player']

    
    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, paddle_sprites):
        super().__init__(groups)

        self.paddle_sprites = paddle_sprites
        self.image = pygame.Surface(SIZE["ball"], pygame.SRCALPHA)
        pygame.draw.circle(self.image, COLORS['ball'], (SIZE['ball'][0]/2, SIZE['ball'][1]/2), SIZE['ball'][0]/2)



        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.old_rect = self.rect.copy()
        self.direction = pygame.Vector2(choice([1,-1]), uniform(0.7, 0.8)*choice([-1,1]))

    def move(self, dt):
        self.rect.center += self.direction * SPEED['ball'] * dt
        self.collision("horizontal")

    def wall_collision(self):
        ## y direction, so top and bottom
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1
    
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1  ## typo, you had 1 instead of -1
      
    def collision(self, direction):
        for sprite in self.paddle_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.rect.right >= sprite.rect.left and self.direction.x == 1:
                        self.rect.right = sprite.rect.left
                        
                    if self.rect.left <= sprite.rect.right and self.direction.x == -1:
                        self.rect.left = sprite.rect.right

                    self.direction.x *= -1



    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
        self.wall_collision()

        
class Opponent(Paddle):
    def __init__(self, groups, ball):
        super().__init__(groups)

        self.speed = SPEED['opponent']
        self.rect.center = POS['opponent']
        self.ball = ball ## this is ball not Ball. we are using the ball passed into the class in init 

    def get_direction(self):
        self.direction = 1 if self.ball.rect.centery > self.rect.centery else -1
