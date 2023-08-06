# _Hangman_ 


![Image of welcome screen](assets/images/welcome-hangman.png)

---
# Introduction

[Hangman](https://github.com/Dekeypetey40/Hangman) is a website where one can play Hangman, a classic game.

This website runs a hangman game created by myself, Kai Michael-Mikhail. The deployed project provides an interactive experience where the user can play against the computer as much or as little as they wish. This was made as my third project as part of Code Institue's Full Stack Developer course.

## Technologies used
- [Python](https://www.python.org/) was the programming language used to create this project.
- [VScode](https://code.visualstudio.com/) was the editor used to write my code.
- [Balsamic](https://balsamiq.com/) was used to make wireframes in the design process.

---

## User stories
- As a first time visitor, I want to easily understand how the game works, so that I become interested in playing it.
- As a first time visitor, I want the website to be easy to interact with, so I can easily have fun playing the game.
- As a user, I want the game to be intuitive to play, so that I can play without trying to figure out how.
- As a user, I want to be able to quit the program, so that I can do something else if I wish. 
- As a returning user, I want to be able to select different difficulty levels, so that I can challenge myself.


---

# Design 
The Element Duel website is designed as a single page site. The page is designed so that minimal scrolling is required. The entirety of the main heading and rules section should fit onto the screen and so should the game area. This is so that one can either read the rules or play the game without having to scroll. This holds true on different devices as well. 

The colour scheme of the site is designed with two shades of blue, which evoke a feeling of calmness. The purpose of this is so that users can relax and enjoy playing the game.

## Planning

### Wireframes

Wireframes were used in the beggining stages of the design phase. 
![Element Duel Wireframe](assets/images/wireframe-ed.png) 

- The rules section was expanded upon as I decided the text in the wireframe was insufficient to explain the rules properly.

---

### Function and variable planning

![Function planning image](assets/images/function-path.png)
- In the planning stages a map of how the user interacts the site was created.
  - It lists the order of events.
  - It lists the functions I predicted I would need.
  - It lists the variables I predicted I would need. 
- In the development process I added a function for the computer to pick an element.
- The displayResult function ended up being spread out between the other functions. 
- Many variables were added so that I could manipulate the text on the DOM and have interactive buttons. 

---

# Features

## Main Page 

![Full Home Page](assets/images/ed-full-page.png)
![Full page mobile](assets/images/ed-full-mobile.png)

### Logo header and rules section

![Full rules image](assets/images/ed-big-rules.png)
- The rules are written concisely, so that the user can quickly and easily understand how the game works.

![Mobile rules image](assets/images/ed-rules-mobile.png)
- On a mobile screen, the rules go from 2 to 1 column to make them easier to read while still fitting onto the screen without scrolling.

---

### Game Area

![Full game area image](assets/images/game-area-big.png)
- The game area is the interactive section of the website.  
- Once the player clicks the begin duel button messages pop up to explain to the user how to proceed. 
- In the results section of the game area the result of each function is shown to the user so that they understand how they go their result.
![Image after duel has begun](assets/images/choose-element-ed.png)
- This indicates to the user that they must now select an element.
- The element buttons are interactive. Once a button is hovered over they get a background colour.
![Fire button](assets/images/fire-button.png)
![Water button](assets/images/water-button.png)
![Nature button](assets/images/nature-button.png)
- When the user clicks on an element button the next promt appears.
![Image after element choice](assets/images/element-choice-made.png)
- The user is promted to roll the dice and their chosen element appears in the results area.
![Final result image](assets/images/final-result.png)
- The final result is shown to the user.
- The Wins and Losses section at the bottom of the game area keeps track of how many times the player wins or loses. 

---

### Footer
![Footer image](assets/images/ed-footer.png) 
- The footer simply indicates the purpose of the website and provides a link to the authors GitHub repositories. 

---

# Future Features
  - An animation of dice being rolled.
  - A player vs player game mode.
  - Adding a best of 5 rounds feature. 

---

# Testing
  - I tested the game countless times using all elements to make sure it functioned as it should
    - When I ran into problems I used console logs to see what the functions were returning. 
  - I tested to make sure the website works in the following browsers: Firefox, Chrome and Edge. 
  - I used Chrome's devtools and [Multi Device Mockup Generator](https://techsini.com/multi-mockup/index.php) to check that the stylings respond and everything functions on all screen sizes. 
  - I tested every button and link to confirm that they work and lead where they are supposed to. 


## Validator testing
* [HTML Validator](https://validator.w3.org/) was run. No errors or warnings were shown. 
![Main page validation](assets/images/html-validation-ed.png)

* [CSS Validator](https://validator.w3.org/) was run and no errors were found, but some minor warnings were attended to. At the time of submission the css code successfully passed the validator with no errors and only minor warnings. 
![css validation](assets/images/css-validation.png)

* Lighthouse in Chrome Developer Tools was used. Initially, there was a low accessibility rating. The cause of this was a lack of aria-labels on the buttons and some html semantic structure. After this was fixed there were no issues.
![Main Page lighthouse](assets/images/lighthouse-element-duel.png)
* [JSHint](https://jshint.com/) was run to check my javascript code. It detected two functions called twice and some missing semicolons. After this no errors were found. 
![JS Validation](assets/images/js-hint-ed.png)

---

## Bugs

## Solved bugs
  - My compare elements function did not work as it should and was not adding 5 to the player who had an advantageous element. This was largely due to the fact that I had called two different functions twice. Once this was fixed the game worked as it should. 
  - When I reformatted my HTML file to be easier to read and then tried to adapt my js file to it the game ceased to function as it should. I undid all my changes and redid the process, checking everything was working with each change I made. This process resulted with the desired effect. 

---

## Unsolved bugs

## Manual Testing

| feature | action | expected result | tested | passed | comments |
| --- | --- | --- | --- | --- | --- |
| Element choice Area | | | | | |
| Element Header | Click the Begin Duel button | InnerText changes from "your fate is yet to be decided" to "choose your element" | Yes | Yes |  |
| Element Header | Click the Roll Dice button | InnerText changes from "choose your element" to one of two options "x element is super effective against y element" or "equal elements" | Yes | Yes |  |
| Fire element button | Click the button | fire becomes the players chosen element, cpuChoice is run, the roll dice button appears and the element header says "Your choice has been made". | Yes | Yes | If user doesn't choose an element the roll dice button does not appear. |
| Water element button | Click the button | water becomes the players chosen element, cpuChoice is run, the roll dice button appears and the element header says "Your choice has been made". | Yes | Yes | If user doesn't choose an element the roll dice button does not appear. |
| Nature element button | Click the button | nature becomes the players chosen element, cpuChoice is run, the roll dice button appears and the element header says "Your choice has been made".  | Yes | Yes | If user doesn't choose an element the roll dice button does not appear. |
| Results area | | | | | |
| Player Side | | | | | |
| Your element | Click on an element button  | Your chosen element appears beside "Your element:"  | yes | yes | |
| You rolled | Click on the roll dice button  | Your random number before bonuses appears beside "You rolled:" | yes | yes | |
| Your bonus | Click on the roll dice button  | A "+5" or "0" appears beside "Your bonus:" depending on if you picked an advantageous element or not | yes | yes | |
| Your final score | Click on the roll dice button  | Your final score after bonuses appears beside "Your final score:" | yes | yes | |
| Opponent Side | | | | |All of these were tested in the same way and have the same expected results except for Opponent Element |
| Opponent Element | Click on an element button and then roll dice  | First cpuChoice is run and a "?" appears beside Opponent element: and then the opponenets element is revealed | yes | yes | |
| Other button area | | | | | |
| Begin Duel | Click the button | You are prompted to choose an element, the button disappears and the reset button appears | Yes | Yes | If you do not click this button you may not select an element  |
| Reset | Click the button | The page reloads | Yes | Yes |  |
| Roll Dice | Click the button | The results of the game are determined and appear in the correct places. | Yes | Yes |  |
| Score Area | | | | | |
| Wins| Test the game until the player wins | 1 is added to the player's wins tally | Yes | Yes | |
| Losses| Test the game until the computer wins | 1 is added to the player's losses tally | Yes | Yes | |
| Footer | | | | | |
| My GitHub link | Click on the link | The link opens up my GitHub repositories in a separate tab | Yes | Yes | |

---

# Deployment
The site was deployed to GitHub pages. The following steps were taken to do so:
1. Log in to [Github](https://github.com/)
2. Navigate to [https://github.com/Dekeypetey40/Element-Duel](https://github.com/Dekeypetey40/Happy-Dog-Website) in the list of repositories
3. In the GitHub repository, navigate to the [Settings](https://github.com/Dekeypetey40/Element-Duel/settings) tab
4. In Settings select [Pages](https://github.com/Dekeypetey40/Element-Duel/settings/pages) on the left hand menu.
5. From the source section drop-down menu, select the main branch.
6. Once the main branch has been selected, click on the save button in the branch section. Wait for the link to be generated and then refresh the page.

---
# Credits


## Content
- A huge thank you to my mentor Aleksei Konovalov for all of his help throughout this process.
- Inspiration for my button design was taken from Code Institute's Love Maths project and was adapted to suit my website.
- The method of functions returning a value as an array was taken from [scaler.com](https://www.scaler.com/topics/javascript-return-multiple-values/).
- The code for the reset button was taken from [Stack Overflow](https://stackoverflow.com/).

---

## Media
  - Icon for my website was taken from [Flaticon](https://www.flaticon.com/)
  - Font Awesome was used for the logo header and the element buttons. 

Creds
Libraries
art 6.0 for ASCII art library https://pypi.org/project/art/
https://blessed.readthedocs.io/en/latest/ to color stuff
Simple Terminal Menu https://pypi.org/project/simple-term-menu/
Wordbank taken from https://github.com/Xethron/Hangman/blob/master/words.txt
The method to replace underscores with letters and print it out inspired by https://www.youtube.com/watch?v=DLurhc1i5_4&ab_channel=MikhaHarly