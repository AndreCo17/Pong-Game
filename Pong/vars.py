import pygame
import random


def init():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    clock = pygame.time.Clock()
    return (clock)

def set_screen():
    screen_width = 1280
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Pong')
    return (screen_width, screen_height, screen)

# Game Rectangle
def game_rectangles(s_w, s_h):
    ball = pygame.Rect(s_w/2-15, s_h/2-15, 30, 30)
    player = pygame.Rect(s_w-20, s_h/ \
                        2-70, 10, 140)  # -70 missing
    opponent = pygame.Rect(10, s_h/2-70, 10, 140)  # -70 missing
    return (ball, player, opponent)


def makeText(text, font, centering, color, dest):
    newText = font.render(text, False, color)
    textRect = newText.get_rect(center=centering)
    dest.blit(newText, textRect)

def escape_menu(s_w, s_h, font, color, allMods):
    menu_font = pygame.font.Font('freesansbold.ttf', 48)
    smolFont = pygame.font.Font('freesansbold.ttf', 16)
    menuBorder = pygame.Surface((s_w/2 + 20, s_h/2 + 20))
    menuBorder.fill(pygame.Color(255, 255, 255))

    menu = pygame.Surface([s_w/2, s_h/2])
    menu.fill(color)
    makeText(f"Pong!", menu_font, (s_w/4, 25), pygame.Color(255, 255, 255), menu)
    makeText(f"Modloading Menu", font, (s_w/4, 75), pygame.Color(255, 255, 255), menu)
    menuPos = (s_w/4 - 10, s_h/4 - 10)

    index = 0
    modSurfaces = []
    for mod in allMods:
        modSurface = mod.makeEscMenuEntry(font, smolFont, (s_w/3, 32), (100, 100 + index*40), pygame.Color(100, 100, 100), menu)
        print(f"{index}: {modSurface}")
        modSurfaces.append(modSurface)
        index += 1

    escText = font.render("[esc]", False, pygame.Color(100, 100, 100))
    menu.blit(escText, (10, 10))

    resetText = font.render("[r]", False, pygame.Color(100, 100, 100))
    menu.blit(resetText, (s_w/2 - 42, 10))

    menuBorder.blit(menu, (10, 10))
    return (menuBorder, menuPos, modSurfaces, smolFont)

def escape_menu_interact(clickPos, modSurfaces, allMods, font, smolFont, s_w, menu):
    index = 0
    for surface in modSurfaces:
        checkingRect = pygame.Rect(surface)
        if checkingRect.collidepoint(clickPos):
            theMod = allMods[index]
            print(f"Clicked on mod: {index}")
            theMod.toggleMod()
            print(theMod)
            theMod.makeEscMenuEntry(font, smolFont, (s_w/3, 32), (110, 110 + index*40), pygame.Color(100, 100, 100), menu)
        index += 1

# Colors
def colors():
    light_grey = (200, 200, 200)
    bg_color = pygame.Color('grey12')
    black = (0, 0, 0)
    money_color = pygame.Color('Green')
    return (light_grey, bg_color, black, money_color)

# Game Variables
def game_vars():
    ball_speed_x = 7 * random.choice((1, -1))
    ball_speed_y = 7 * random.choice((1, -1))
    player_speed = 0
    opponent_speed = 3
    return (ball_speed_x, ball_speed_y, player_speed, opponent_speed)

# Score Text
def scoring_text():
    player_score = 0
    opponent_score = 0
    basic_font = pygame.font.Font('freesansbold.ttf', 32)
    return (player_score, opponent_score, basic_font)

# Sound Variables
def sounds():
    pong_sound = pygame.mixer.Sound("./media/pong.ogg")
    score_sound = pygame.mixer.Sound("./media/score.ogg")
    return (pong_sound, score_sound)
### Modloader Connection Bits (DO NOT EDIT PLEASE): [class Mod, def emptyFunc, class modInputs, def mods]

# Modloader Mod handler
class Mod:
    def __init__(self, name, creator, loadMethod, loadParams, unloadMethod, unloadParams, textColor, mod=""):
        self.name = name
        self.creator = creator
        self.activate = loadMethod
        self.activateParams =loadParams
        self.deactivate = unloadMethod
        self.deactivateParams = unloadParams
        self.textColor = textColor
        self.surface = ""
        self.mod = mod
        self._isOn = False
    
    def toggleMod(self):
        self._isOn = not self._isOn
        if self._isOn:
            self.activate(self.activateParams)
        else:
            self.deactivate(self.deactivateParams)
    
    def isOn(self):
        return self._isOn

    def makeEscMenuEntry(self, font, smolFont, size, pos, bgcolor, dest):
        onText = "[  ]"
        if self._isOn:
            bgcolor = (100, 150, 100)
            onText = "[X]"

        newSurface = pygame.Surface(size)
        newSurface.fill(bgcolor)
        displayText = font.render(f"{onText}  {self.name}", False, self.textColor)
        newSurface.blit(displayText, (20, -1))
        nameSurface = displayText.get_rect().size

        creatorText = smolFont.render(f"by {self.creator}", False, self.textColor)
        newSurface.blit(creatorText, (nameSurface[0] + 30, 13))

        
        print(f"ModName Surface: {nameSurface}")
        dest.blit(newSurface, pos)
        myPos = (pos[0] + 320, pos[1] + 200, size[0], size[1])

        self.surface = newSurface

        return myPos

    def __str__(self) -> str:
        return f"{self.name} - Activated: {self._isOn}"

# Empty Function, use as "necessary"
def emptyFunc(params):
    pass

# ModInputs, provides a class for slightly more guideance in what to pass to the Modloader
class ModInputs:
    def __init__(self, name, creator, loadMethod, loadParams, unloadMethod, unloadParams, textColor, mod):
        self.name = name
        self.creator = creator
        self.loadMethod = loadMethod
        self.loadParams =loadParams
        self.unloadMethod = unloadMethod
        self.unloadParams = unloadParams
        self.textColor = textColor
        #self.surface = None
        self.mod = mod

# mods function takes the parameters (0 is empty function, basically starting at 1) and turns them into the Modloader mods
def mods(modFunctionItems):
    emptyFunc: function = modFunctionItems[0]
    
    allMods = []

    index = 1
    while index < len(modFunctionItems):
    
        newMod = Mod(modFunctionItems[index].name,
                    modFunctionItems[index].creator,
                    modFunctionItems[index].loadMethod,
                    modFunctionItems[index].loadParams,
                    modFunctionItems[index].unloadMethod,
                    modFunctionItems[index].unloadParams,
                    modFunctionItems[index].textColor
                    )
        allMods.append(newMod)
        modFunctionItems[index].mod.connectToMod(newMod)
        index += 1
    
    return allMods
