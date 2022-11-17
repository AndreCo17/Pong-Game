# Pong Mods
## Space Mod
### Author
Terrence

### Description
Toggling the mod on changes the background image, paddle images, and ball image to space themed ones.

### Does this improve gameplay?
Yes. In the same way that people enjoy paying to theme their games to their liking, this mod provides another theme option for the game. It also helps encourage the player to use their imagination.
One aspect of video games that people enjoy, is their level of interesting visual elements. Some games implement extremely realistic graphics to emerse users while others focus on specific art styles not intended to replicate reality for the same reasons.

## Sounds Mod
### Author
Mark

### Description
Toggling this mod allows users to have music added to their play experience along with muting functionality

### Does this improve gameplay?
As sound is a key component to any game, allowing users to customize their experience with sound settings also improves the gameplay and increases playability.

## Countdown Mod
### Author
Andre

### Description
Add a countdown delay when starting another round after one player misses the ball.

### Does this improve gameplay?
Instantly restarting the game is very jaring for the player because people take time to switch tasks or reorient themselves.
The delay in sending the ball after loosing a round allows the human player some time to reorient themselves and prepare for the next round.

## Set Score Goal Mod
### Author
Lorenzo

### Description
![Mod selection screen](https://github.com/eightys3v3n/comp_4555/blob/main/Pong/media/readme-enzo-1.png?raw=true)  
When the "Set Score Goal" is enabled, the user will be asked to enter a value and set it as a score goal that both the opponent and the player must achieve.  
![Enter winning score interface](https://github.com/eightys3v3n/comp_4555/blob/main/Pong/media/readme-enzo-2.png?raw=true)  
When either reaches the set score goal, the game declares a winner and shows an exit button.
The player can also press r to restart.  
![Winner screen](https://github.com/eightys3v3n/comp_4555/blob/main/Pong/media/readme-enzo-3.png?raw=true)  

### Does this improve gameplay?
Yes, as the original game is set to play for infinity where no winner will be declared (unless either player is unable to continue). Adding this mod, it would allow the game to run for a specific amount of time and also adds a little bit of challenge to allow the player to focus on reaching the set score before the opponent. 

## Modloader / Sample Mod
### Author
Mihai

### Description
The modloader provides the ability to load and unload various mods using a consistent interface. It also implements a pause menu with 'esc' and restart functionality with 'r'. The pause menu has a list of mods where the user can select or unselect them to toggle them in-game.
    The basic view that players would see at the start of the game without any extra mods added in:
![Basic Modloader Interface](https://github.com/eightys3v3n/comp_4555/blob/main/Pong/media/readme-mihai-1.png?raw=true)
    When all our mods are added into the modloader:
![Filled Modloader Interface](https://github.com/eightys3v3n/comp_4555/blob/main/Pong/media/readme-mihai-2.png?raw=true) 
    Say I want to toggle on Space Graphics by Terrence and Sounds Mod by Mark, I click on the entrys to turn them on. Yee-Haw!
![Filled Modloader Interface](https://github.com/eightys3v3n/comp_4555/blob/main/Pong/media/readme-mihai-3.png?raw=true) 

A sample mod is provided (changing the colour of the paddles and ball) as an example for everyone else in the group to understand how to make a mod that is compatible with the modloader.
    Turning on the Sample Mod by Mihai makes the gameplay colorful!
![Sample Mod Screenshot](https://github.com/eightys3v3n/comp_4555/blob/main/Pong/media/readme-mihai-4.png?raw=true)


### Does this improve gameplay?
The modloader allows for anyone who reads the sample mod documentation (and a bit within the 9-pong.py) to connect their mod to the game in an easier way, rather than coding directly into the main game file. This functionality provides a consistent and predictable way to interact with mods that might otherwise be complex to turn on and off. This provides the player a more refined modding experience.
The ability for the player to pause and restart the game is also pretty important features as most players would expect the ability to do these things.
Sample mod is a simple version of theming the game. Players would enjoy it for the same reasons they might enjoy the Space mod.
