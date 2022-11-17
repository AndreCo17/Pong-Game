import pygame 
import random

class timer:

    game_time = True

    def __init__(self):
        self.isOn = False

    def activate(self, params):
        self.isOn = True

    def deactivate(self, params):
        self.isOn = False
        
    def connectToMod(self, modIn):
        self.mod = modIn

    def setCountdown(self, game_time, ball_speed_x, ball_speed_y, 
                     basic_font, timer_color, screen_height, screen_width, screen):
        
        if self.isOn:
            current_time = pygame.time.get_ticks()

            if current_time - game_time < 1000:
                number_three = basic_font.render("3",False,timer_color)
                screen.blit(number_three,(screen_width/2 - 10, screen_height/2 + 20))
        
            elif 1000 < current_time - game_time < 2000:
                number_two = basic_font.render("2",False,timer_color)
                screen.blit(number_two,(screen_width/2 - 10, screen_height/2 + 20))
        
            elif 2000 < current_time - game_time < 3000:
                number_one = basic_font.render("1",False,timer_color)
                screen.blit(number_one,(screen_width/2 - 10, screen_height/2 + 20))

            elif current_time - game_time < 3000:
                ball_speed_y, ball_speed_x = 0,0
                
            else:
                ball_speed_y = 7 * random.choice((1, -1)) 
                ball_speed_x = 7 * random.choice((1, -1)) 
                game_time = None
                
            return ball_speed_x, ball_speed_y, game_time
        
        else:
            ball_speed_y = 7 * random.choice((1, -1)) 
            ball_speed_x = 7 * random.choice((1, -1)) 
            
            return ball_speed_x, ball_speed_y, game_time
        
def makeMod():
    return timer()

    