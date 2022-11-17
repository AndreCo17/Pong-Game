import pygame 

# Create a surface for the scores
def surface(font, p_score, o_score, color, screen):
    player_text = font.render(f"{p_score}", False, color)
    screen.blit(player_text, (660,470))

    opponent_text = font.render(f"{o_score}", False, color)
    screen.blit(opponent_text, (600,470))