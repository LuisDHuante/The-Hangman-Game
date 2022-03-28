# The Hangman Game 
1.0 <br/>
This is a simple implementation of the hangman game with Python 3. 
## Main Menu
 
![portada](https://user-images.githubusercontent.com/69726163/160447681-6aad3645-2dd8-4de5-a62a-fa60343f654b.jpg)

The main menu has 4 different options

1. Start game
2. Add word to the game
3. Credits
4. Quit

## 1. Start game
The first option leads us to game menu:

![image](https://user-images.githubusercontent.com/69726163/160448659-468839fc-4c69-4693-9f04-c91ea93f9bed.png)

The game menu has 4 different options:

1. Safe mode
2. Danger mode
3. Instructions
4. Return to main menu

### Safe mode
In Safe mode, you have infinite lives, which means you can try any number of letters to win the game.

![image](https://user-images.githubusercontent.com/69726163/160449103-71a990c3-0105-440b-b471-ba07d9219414.png)

### Danger mode
In Danger mode, you have a limited amount of attempts (10 lives) to guess the word and save the hangman.
![image](https://user-images.githubusercontent.com/69726163/160449767-c8290c64-4237-41a6-8fcd-6dc47bca0998.png)

## 2. Add word to the game
You can also add any word you like to the game. The game detects if you insert invalid characters and only accepts the alphabetic ones.
The new words are added directly to the 'data.txt' file.
![image](https://user-images.githubusercontent.com/69726163/160450704-c39ede6b-7ed2-4e89-9908-00bedb32bad6.png)
![image](https://user-images.githubusercontent.com/69726163/160450863-e7a40fd1-1076-465d-899f-ca998c8635c8.png)


## Error and exception handling
1. In any of the menus, you cannot enter an invalid option <br/>
![image](https://user-images.githubusercontent.com/69726163/160451346-a2063de0-259f-4e23-9918-3121413c8d31.png)
2. While playing, you canot enter invalid characters. This is what the screen displayed after entering the number 3.
![image](https://user-images.githubusercontent.com/69726163/160451599-0c7d9ba0-fa22-4f51-aa9c-626a95962d56.png)
3. You cannot enter numbers or special characters in the Add word section <br/>
![image](https://user-images.githubusercontent.com/69726163/160451851-37c4641b-f411-4c73-89bb-189be38e579c.png)


