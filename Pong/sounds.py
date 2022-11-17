import pygame
import sys

class sounds:

    def __init__(self, screen, screen_width):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        self.screen = screen
        self.screen_width = screen_width
        self.space_song = pygame.mixer.Sound("./media/background.mp3")
        self.sfx = "./media/sfx.png"
        self.sfxmute = "./media/sfxmute.png"
        self.music = "./media/music.png"
        self.musicmute = "./media/musicmute.png"
        self.sfximage = self.sfx
        self.musicimage = self.music
        self.isOn = False
        self.music_bool = True
        self.sfx_bool = False

    def activate(self, params):
        self.isOn = True

    def deactivate(self, params):
        self.isOn = False
        self.muteMusic(True)
        self.stop_music()
        self.muteSFX(False)


    def connectToMod(self, modIn):
        self.mod = modIn

    ## Accessors
    def isSFXMuted(self):
        return self.sfx_bool

    def isMusicMuted(self):
        return self.music_bool

    ## Mutators
    def muteSFX(self, bool):
        self.sfx_bool = bool

    def muteMusic(self, bool):
        self.music_bool = bool

    # Play/Stop Music
    def play_music(self):
        if(self.isOn):
            pygame.mixer.Sound.play(self.space_song)

    def stop_music(self):
        pygame.mixer.Sound.stop(self.space_song)

    ## Helpers

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                if(self.isMusicMuted() == False):
                    self.stop_music()
                    self.muteMusic(True)
                    print(self.isMusicMuted())
                else:
                    self.play_music()
                    self.muteMusic(False)
                    print(self.isMusicMuted())
            if event.key == pygame.K_n:
                if(self.isSFXMuted() == False):
                    self.muteSFX(True)
                    print(self.isSFXMuted)
                else:
                    self.muteSFX(False)
                    print(self.isSFXMuted())

    def  getSFXImage(self, mute):
        if(self.isOn):
            #switch image based on mute bool
            if(mute == True):
                image = pygame.image.load(self.sfxmute)
            if(mute == False):
                image = pygame.image.load(self.sfx)
            return (image)

    def getMusicImage(self, mute):
        if(self.isOn):
            #switch image based on mute bool
            if(mute == True):
                image = pygame.image.load(self.musicmute)
            if(mute == False):
                image = pygame.image.load(self.music)
            return (image)

    def draw_btns(self):
        if(self.isOn):
            #loading sfx image
            myimage = self.getSFXImage(self.sfx_bool)
            myimage = pygame.transform.scale(myimage, (50,50))
            imagerect = myimage.get_rect()
            imagerect = imagerect.move((self.screen_width-150,75))
            self.screen.blit(myimage, imagerect)

            #loading sfx text
            myimage = pygame.image.load("./media/N.png")
            myimage = pygame.transform.scale(myimage, (50,50))
            imagerect = myimage.get_rect()
            imagerect = imagerect.move((self.screen_width-150,125))
            self.screen.blit(myimage, imagerect)

            #loading music image
            myimage = self.getMusicImage(self.music_bool)
            myimage = pygame.transform.scale(myimage, (50,50))
            imagerect = myimage.get_rect()
            imagerect = imagerect.move((self.screen_width-75,75))
            self.screen.blit(myimage, imagerect)

            #loading sfx text
            myimage = pygame.image.load("./media/M.png")
            myimage = pygame.transform.scale(myimage, (50,50))
            imagerect = myimage.get_rect()
            imagerect = imagerect.move((self.screen_width-75,125))
            self.screen.blit(myimage, imagerect)

def makeMod(screen, screen_width):
    return sounds(screen, screen_width)