import pygame


""" Credits
Platforms: https://www.pngwing.com/en/free-png-xszbz
Ball: https://www.pngwing.com/en/free-png-poxad
Planet Ball: https://www.pngwing.com/en/free-png-pyqkc/download
Background Blue: https://www.pngwing.com/en/free-png-zogqw
Background Brighter: https://www.pngwing.com/en/free-png-zpeir
"""


class sampleMod:
    def __init__(self, *, ball, player, opponent):
        self.background_img = pygame.image.load('media/background-brighter.png')
        self.background_img = pygame.transform.scale(self.background_img, pygame.display.get_window_size())

        self.ball = ball
        self.ball_img = pygame.image.load('media/ball_planet.png')
        self.ball_img = pygame.transform.scale(self.ball_img, (ball.width, ball.height))

        self.player = player
        self.player_img = pygame.image.load('media/paddle.png')
        self.player_img = pygame.transform.scale(self.player_img, ((pygame.display.get_window_size()[0] - player.x - player.width) + player.width, player.height))

        self.opponent = opponent
        self.opponent_img = pygame.image.load('media/paddle.png')
        self.opponent_img = pygame.transform.flip(self.opponent_img, True, False)
        self.opponent_img = pygame.transform.scale(self.opponent_img, (opponent.x + opponent.width, opponent.height))
        self.isOn = False

    def activate(self, params):
        self.isOn = True

    def deactivate(self, params):
        self.isOn = False
        
    def connectToMod(self, modIn):
        self.mod = modIn

    def draw(self, screen):
        if self.isOn:
            screen.blit(self.background_img, (0, 0))
            screen.blit(self.ball_img, (self.ball.x, self.ball.y))
            screen.blit(self.player_img, (self.player.x, self.player.y))
            screen.blit(self.opponent_img, (self.opponent.x - self.opponent.width, self.opponent.y))

        
def makeMod(**kwargs):
    return sampleMod(**kwargs)