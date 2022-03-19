# Four Letter Wordle
Four Letter Worlde is a bootleg version of the popular vocabulary game [Wordle](https://www.nytimes.com/games/wordle/index.html). Like the title suggests, this version involves the usage of only four letter words, instead of the original five. Additionally, instead of the original six tries allowed, this version allows only five tries.

![demo](https://user-images.githubusercontent.com/88521066/159120146-2385183e-36fd-48e7-b9b1-a727ad6ee1b1.gif)

Four Letter Wordle was created as a training project to gain familiarity with the Python library, Pygame.

## The Rules of the Game
Four Letter Wordle essentially follows most of the same rules as the official Wordle. The premise of the game is to correctly guess the answer word within a number of tries. After each guess, the squares corresponding to each letter are colored differently, hinting at how close the player's guess is to the correct word. There are three colors the squares can take
- :green_square: implies that the letter is the correct spot
- :orange_square: implies that the letter is the incorrect spot but is a letter in the answer word
- :black_large_square: (which is actually a dark grey) implies that the letter is not only in the incorrect spot but also is not in the answer word at all 

## Nuanced Explaination for Coloring of Squares
To illustrate how the coloring of squares is utilized in Four Letter Wordle, here are some example cases.

![case_one](https://user-images.githubusercontent.com/88521066/159120060-1e818408-aed0-4fb4-92ec-89f08cad1c0b.gif)

#### The Single - Multiple
Consider the case where the answer word is *'DOLE'* and the player guesses *'POOL'*. The first *O* will be with a green squares as it corresponds to the correct second letter of *DOLE*. The second *O* will be with a dark grey square as there are no more remaining *O*s in the answer. Despite the answer *DOLE* having an *O*, the second *O* in *POOL* appears with a dark grey (incorrect) square as the first *O* was already marked as in the correct position.

#### The Multiple - Single 
Consider the case where the answer word is *MOON* and the player guesses *DOGS*. In this case, the *O* in *DOGS* will be with an green square as it is in the correct position.

#### The Multiple - Multiple 
Consider the case where the answer word is *SOON* and the player guessed *ODOR*. In this case, the first *O* in *ODOR* will be with an orange square, while the *O* in index 2 of *ODOR* will be with a green square. This particular case is different than that of the first **Single - Multiple** case as the answer word contains two *O*s just as the guess does. 

## How does Four Letter Wordle check the guess?

There are two main questions to ask when checking the player's guess. 
- Is this guess an actual word?
- Is this letter in the correct position?

### Is this guess an actual word?

This is checked by looking if the guess is in the words.words() from the NLTK library. As words.words() only contains singular form of words, the addition of 's' at the end of words to make them plural must be accounted for as well.

### Is this letter in the correct position?

It is obvious when the letter is in the correct position or a letter is not in the answer word at all. The case a letter is in the incorrect position and there are multiples of it (whether it be multiples of a letter in the answer word or guess), function find_many() is utilized to find positions of the letter in question. By finding the positions and counting the letters, the orange or dark grey squares are colored correctly per official Wordle game rules.

## Usage

Download Four Letter Wordle by cloning this repo

```
git clone https://github.com/ichennnn/four-let-wordle.git
```

### How to Run?

```
cd four-let-wordle
python game_app.py
```

## Python Libraries Used

Python 3.8.8
- Selenium, Pygame, Pandas, NLTK, random, os

## Acknowledgements

This bootleg version of Wordle was based on LeMaster Tech's (on YouTube) [video](https://www.youtube.com/watch?v=D8mqgW0DiKk) with modifications including the change from five letter words to four letters as well as other tweaks to make Four Letter Wordle emulate the official Wordle's game rules and game play in greater detail.

While the official Wordle draws upon a a five-letter word list, Four Letter Wordle draws upon a four letter word list which was webscraped from this [website](https://eslforums.com/4-letter-words/)
