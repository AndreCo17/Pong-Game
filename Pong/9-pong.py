import pygame
import random
import sys
import vars
import enzoMod
import score_surface
import sampleMod
import sounds
import terrence_mod
import timer


# GLOBAL VARIABLES

game_time = True

# Initialization of PyGame :)
clock = vars.init()

# Screen Variables
(screen_width, screen_height, screen) = vars.set_screen()

# Game Rectangle
(ball, player, opponent) = vars.game_rectangles(screen_width, screen_height)

# Colors
(light_grey, bg_color, escMenuColor, timer_color) = vars.colors()

# Game Variables
(ball_speed_x, ball_speed_y, player_speed, opponent_speed) = vars.game_vars()

# Score Text
(player_score, opponent_score, basic_font) = vars.scoring_text()

# Sound Variables
(pong_sound, score_sound) = vars.sounds()

### Mods Area ###
# Instantiate mods here
sample = sampleMod.makeMod(ball_speed_x, light_grey)
enzo = enzoMod.makeMod(screen, screen_width, screen_height, '', '')
terrence = terrence_mod.makeMod(ball=ball, player=player, opponent=opponent)
timer = timer.makeMod()
soundsMod = sounds.makeMod(screen,screen_width)

#Game modload menu list of mods (add your mod connection stuffs here)
modFunctionItems = [
    vars.emptyFunc,
    #vars.ModInputs("Example", "Author", vars.emptyFunc, (), vars.emptyFunc, (), (0, 0, 0), InserModObjectHere!),
    vars.ModInputs("Sample Mod", "Mihai", sample.activate, (), sample.deactivate, (), (50, 0, 50), sample),
    vars.ModInputs("Countdown", "Andre", timer.activate, (), timer.deactivate, (), (0, 50, 0), timer),
    vars.ModInputs("Space Graphics", "Terrence", terrence.activate, (), terrence.deactivate, (), (100, 0, 0), terrence),
    vars.ModInputs("Set Score Goal", "Lorenzo", enzo.activate, (), enzo.deactivate, (), (50, 0, 50), enzo),
    vars.ModInputs("Sounds Mod", "Mark", soundsMod.activate, (), soundsMod.deactivate, (), (50, 0, 50), soundsMod)
]

#Set up the modload menu
allMods = vars.mods(modFunctionItems)


# Escape Menu
(menu, menuPos, modSurfaces, smolFont) = vars.escape_menu(screen_width, screen_height, basic_font, escMenuColor, allMods)

# FUNCTIONS



def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, game_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball Collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Ball Collision Left
    if ball.left <= 0:
        if(soundsMod.isSFXMuted() == False):
            pygame.mixer.Sound.play(score_sound)
        player_score += 1
        game_time = pygame.time.get_ticks() - 1000
        ball_restart()

    # Ball Collision Right
    if ball.right >= screen_width:
        if(soundsMod.isSFXMuted() == False):
            pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        game_time = pygame.time.get_ticks() - 1000
        ball_restart()


    # Ball Collision (Player)
    if ball.colliderect(player) or ball.colliderect(opponent):
        if(soundsMod.isSFXMuted() == False):
            pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1


def player_animation():
    global player_speed

    player.y += player_speed

    # Player Collision
    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
  global opponent_speed

  if opponent.top < ball.top : #opponent is above ball
      opponent.y += opponent_speed

  if opponent.bottom > ball.bottom: # opponent is below ball
      opponent.y -= opponent_speed

  if opponent.top <= 0:
      opponent.top = 0

  if opponent.bottom >= screen_height:
      opponent.bottom = screen_height

  
def ball_restart():
    global ball_speed_x, ball_speed_y, game_time

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x, ball_speed_y, game_time = timer.setCountdown(game_time, ball_speed_x, ball_speed_y, basic_font, timer_color, screen_height, screen_width, screen)


if __name__ == "__main__":
    #initialize variable to store winning score.
    winScore = None
    paused = True
    soundsMod.play_music()

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if enzo.isOn:
                title = 'Enter Winning Score: '
                winScore = enzo.drawInputBox(screen, screen_width, screen_height, title, event)
                paused = not paused
                enzo.deactivate(True)

            soundsMod.handleEvent(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed -= 6
                elif event.key == pygame.K_DOWN:
                    player_speed += 6
                elif event.key == pygame.K_ESCAPE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    ball_restart()
                    player_score = 0
                    opponent_score = 0
                    opponent.top = screen_height/2-70
                    player.top = screen_height/2-70

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_speed += 6
                if event.key == pygame.K_DOWN:
                    player_speed -= 6

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and paused:
                pos = pygame.mouse.get_pos()
                #print(f"Click: {pos}")
                vars.escape_menu_interact(pos, modSurfaces, allMods, basic_font, smolFont, screen_width, menu)

        #If either player or the opponent won, set winner variable.
        if winScore == player_score:
            paused = True
            winner = 'Player'
        if winScore == opponent_score:
            paused = True
            winner = 'Opponent'

        if not paused:
            ball_animation()
            player_animation()
            opponent_ai()

        ballColor = sample.setBall(ball_speed_x)
        playerColor = sample.setPlayer()
        opponentColor = sample.setOpponent()

        if terrence.isOn:
            terrence.draw(screen)
        else:
            screen.fill(bg_color)
            pygame.draw.rect(screen, playerColor, player)
            pygame.draw.rect(screen, opponentColor, opponent)
            pygame.draw.ellipse(screen, ballColor, ball)

        pygame.draw.aaline(screen,
                           light_grey,
                           (screen_width/2, 0),
                           (screen_width/2, screen_height)
        )


          # Create a surface for the scores
        player_text = basic_font.render(f"{player_score}", False, light_grey)
        screen.blit(player_text, (660,470))

        opponent_text = basic_font.render(f"{opponent_score}", False, light_grey)
        screen.blit(opponent_text, (600,470))

        score_surface.surface(basic_font, player_score, opponent_score, light_grey, screen)

        if game_time and timer.isOn:
            ball_restart()

        #If either the player or the opponent won, pass declare the winner
        if paused:
            if player_score != winScore and opponent_score != winScore:
                screen.blit(menu, menuPos)

            if player_score == winScore or opponent_score == winScore:
                enzo.declareWinner(screen, screen_width, screen_height, winner, event)
            #Opens the Mod Menu if game is paused and the opponent and player has not reached the score goal

        soundsMod.draw_btns()

        pygame.display.flip()
        clock.tick(60)
