# The Riddles Project

A web application game that asks players to guess the answer to a text-based riddle. This is a logic driven application.

The player is presented with text that contains the riddle. Players enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly they are redirected to the next riddle.
If a player guesses incorrectly their incorrect guess is stored and printed below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time. Users are identified by a unique username.
There is  a leaderboard that ranks top scores for all users.
 
## UX
 
I chose to go with one image for the game to keep it simple, and aligned it to the center for aesthetics.
## Features

users can input unique user name
scores are presented at the end of the game
users can input their answers in text area
 
### Existing Features

a responsive, mobile first design.
Game Logic - allows three attempts


## Technologies Used


Backend

Python3
Flask

Frontend

HTML5
CSS3
Bootstrap 
jQuery 

## Testing

I played the game repeatedly under different names to see if all the notifications came up and to verify the leaderboard was working. I also tested the game on various devices

## Deployment
I tried to use heroku ps:scale web=1
but got this message couldn't find that process type (web) when scaling dynos 

so i Installed gunicorn

Created Procfile

Updated requirements.txt

Logged in to heroku

Initialise git and set a remote for heroku

Pushed to Heroku

## Credits
yoniLavi/ci-pp-milestone-riddlemethis

### Media
- The photos used in this site were obtained from pixabay

### Acknowledgements

- I received inspiration for this project from CodeInstitute project outline
   
