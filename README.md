# Hangman-the-game

Upgraded project of Jetbrains Academy. 
The world famous word guessing game. You will have 8 attempts to guess the word. A word is chosen randomlly from a list of 10000 random words. The description of a word provided in the beginning of a game. Have Fun!

# Requirements

pip3 install requests  
pip3 install PyDictionary

I used the requests library to connect to a list of words that is in the public domain. In adittion, requests is used to get the meaning of a word. PyDictionary is deployed for security purposes when the output of a request results in an error.

