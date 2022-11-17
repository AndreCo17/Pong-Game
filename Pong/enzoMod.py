##### Documentation for mods:
#
# Your mod should be within a class, that provides at least these methods:
#     __init__
#         pass in anything your mod needs from the start here
#     activate(params)
#         This should at least turn on your mod internally
#         the params are required as a parameter but are optional to be used,
#           pass in anythin required upon activation (screen, maybe?)
#     deactivate(params)
#         This should at least turn off your mod internally
#         the params are required as a parameter but are optional to be used,
#           pass in anythin required upon activation (delete anything that
#           is not in the base game here)
#     connectToMod(modIn)
#         Please have this method here, even if you may not use it. This is
#           to allow you to look at the properties of the modloader's version
#           of your mod
#
# Additionally, you should add a makeMod function at the end of your module
#   that takes the same parameters as your __init__ method and returns your
#   new mod object that it makes.
#
#                                          Thanks for reading, happy modding!
#                                                                - Mihai Popa
#
# from asyncio.windows_events import NULL
import pygame,sys
class enzoMod:
    def __init__(self, screen, s_w, s_h, winner, title):
        self.screen = screen
        self.s_w = s_w
        self.s_h = s_h
        self.winner = winner
        self.title = title
        self.isOn = False

    def activate(self, params):
        self.isOn = True

    def deactivate(self,params):
        if params:
            self.isOn = False
        
    def connectToMod(self, modIn):
        self.mod = modIn

    def declareWinner(self, screen, s_w, s_h, winner, event):    
        #set Base Font
        base_font = pygame.font.Font(None, 32)
        
        #Set text for the Title 
        winner_text = winner + ' is the Winner!'
        
        #Set the shape and color on where the Title will go
        winner_rect = pygame.Rect(s_w/2 - 140, s_h/2 - 16, 280, 32)
        winner_color= pygame.Color('firebrick1')

        #Initialize the shape for the interactive button
        exitButton_rect = pygame.Rect(s_w/2 -30, s_h/2 +32, 60, 32)              
        
        #initialize the colors for when user clicks the button
        exitButton_active= pygame.Color('blue3')
        exitButton_passive= pygame.Color('dodgerblue1')
        exitButton_color = exitButton_passive
        exitButton_color = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exitButton_rect.collidepoint(event.pos):
                exitButton_color = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if exitButton_rect.collidepoint(event.pos):
                    exitButton_color = False
                        
        if exitButton_color:
            exitButton_color = exitButton_active
        else:
            exitButton_color = exitButton_passive

        #Draw the shape on the screen and place the text
        pygame.draw.rect(screen, winner_color, winner_rect)
        pygame.draw.rect(screen, exitButton_color, exitButton_rect)
        
        winner_surface = base_font.render(winner_text, True, 'cyan1')
        screen.blit(winner_surface, (winner_rect.x+10, winner_rect.y+5))
        
        #auto adjust the shape to accomodate the Title texts
        winner_rect.w = max(100, winner_surface.get_width() + 10)

        exitButton_surface = base_font.render('Exit', True, (255,255,255))
        screen.blit(exitButton_surface, (exitButton_rect.x+5, exitButton_rect.y+5))
        exitButton_rect.w = max(100, exitButton_surface.get_width() + 10)
        
    #Load the screen to enter input from users
    def drawInputBox(self, screen, s_w, s_h, title, event):    
            
        pygame.init()
        clock = pygame.time.Clock()
        
        screen = pygame.display.set_mode([s_w, s_h])
        base_font = pygame.font.Font(None, 32)
        title_text = title
        user_text = ''
        button_text = 'Done'
        
        #Initialize shape for user input box
        input_rect = pygame.Rect(s_w/2 -70, s_h/2 -20, 140, 32)
        
        #Initialize colors for user interaction with the input box
        input_color_active= pygame.Color('deepskyblue2')
        input_color_passive= pygame.Color('gainsboro')
        input_color = input_color_passive
        
        #This will disable the user input box at the beginning
        input_active = False

        #Initialize the shape and color for the title box
        title_rect = pygame.Rect(s_w/2 -97.5, s_h/2 -50, 195, 32)
        title_color= pygame.Color('darkslategray3')

        #Initialize the shape for the interactive button
        button_rect = pygame.Rect(s_w/2 -30, s_h/2 +16, 60, 32)
        
        #initialize the colors for when user clicks the button
        button__color_active= pygame.Color('blue3')
        button__color_passive= pygame.Color('dodgerblue1')
        button_color = button__color_passive

        button_active = False

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                #This will enable the input box if user clicks on it. Hence, 
                #the input box will only receive input if it's active
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        input_active = True
                    else:
                        input_active = False    
                #If the backspace is pressed, remove the last unicode entered from the input box
                #otherwise, collect user input.
                if event.type == pygame.KEYDOWN:
                    if input_active == True:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        elif event.unicode.isdigit():
                            user_text += event.unicode
                #if the user clicks the button, pass the variable to the main program
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        button_active = True
                        return int(user_text)
                if event.type == pygame.MOUSEBUTTONUP:
                    if button_rect.collidepoint(event.pos):
                        self.isOn = False
            
            screen.fill((0,0,0,))
            
            if input_active:
                input_color = input_color_active
            else:
                input_color = input_color_passive
            
            if button_active:
                button_color = button__color_active
            else:
                button_color = button__color_passive
                
            pygame.draw.rect(screen, input_color, input_rect,2)
            pygame.draw.rect(screen, button_color, button_rect)
            
            
            title_surface = base_font.render(title_text, True, title_color)
            screen.blit(title_surface, (title_rect.x+5, title_rect.y+5))
            
            input_surface = base_font.render(user_text, True, (255,255,255))
            screen.blit(input_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(140, input_surface.get_width() + 10)
                
            button_surface = base_font.render(button_text, True, (255,255,255))
            screen.blit(button_surface, (button_rect.x+5, button_rect.y+5))
            button_rect.w = max(40, button_surface.get_width() + 10)
            
            pygame.display.flip()
            clock.tick(60)
    
        
def makeMod(screen, s_w, s_h, winner, title):
    return enzoMod(screen, s_w, s_h, winner, title)