# Hangman - Revisited

It is the year 2034.
The COVID pandemic rages on.
People around the world have exhausted their supply of entertainment and are now turning to other sources to cure their boredom.
One game stands out above all others in providing people with endless joy: Hangman.

Here at Hangman Hubs, we empower strangers, friends, coworkers, families, and people that have oddly close relationships with their pets to connect to each other at a deeper level.
We do that through the classic game of hangman.

If you don’t know what hangman is, no worries!
It’s a simple word game where the player has a limited number of chances to guess a random word.

Here are the rules:

- A random word is chosen at the beginning of the game.
- The word is hidden from the player.
- The player has to guess, one letter at a time, what the word is.
- Each successful guess will reveal the letter in the hidden word.
- If they guess incorrectly 5 times, then it’s game over.
- If they guess the word correctly and the whole word is revealed, they win!

## Game components

It's split into two projects:

- [hangman-server](hangman-server)
- [hangman-web-app](hangman-web-app)

## Getting started

Get the server up and running

```
cd hangman-server
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
python server.py
```

Get the web-app running

```
cd hangman-web-app
npm install
npm run start
```

Play some hangman!

```
http://localhost:3000
```

Good luck and have fun!
