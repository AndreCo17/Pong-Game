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

class sampleMod:
    def __init__(self, ballX, gray):
        self.ballSpeed = ballX
        self.lastReboundTick = 0
        self.gray = gray
        self.player = (100, 100, 150)
        self.opponent = (150, 100, 100)
        self.isOn = False

    def activate(self, params):
        self.isOn = True

    def deactivate(self, params):
        self.isOn = False
        
    def connectToMod(self, modIn):
        self.mod = modIn

    def setBall(self, ballX):
        if self.isOn:
            if ballX > 0:
                return self.opponent
            else:
                return self.player
        else:
            return self.gray

    def setPlayer(self):
        if self.isOn:
            return self.player
        else:
            return self.gray
        

    def setOpponent(self):
        if self.isOn:
            return self.opponent
        else:
            return self.gray
        
def makeMod(ballX, gray):
    return sampleMod(ballX, gray)