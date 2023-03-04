
# Cursed Island

![App Screenshot](https://www.simpleimageresizer.com/_uploads/photos/fd48d8b6/cursedlogo2_99.png)


Cursed Island is a classic text-based adventure game inspired from the classic ones from the late late seventies like Zork and Stugan(The Cottage).

[Live Link to the project](https://cursed-island.herokuapp.com/)


## Instructions

You will face different encounters that will leave you with two choices.
pressing the letter marked between the () brackets, Will lead you into a new scenario.

if you survive all scenarios you win the game!
## Features

- Colored text and cool ASCII-Art
- Multiple choice scenarios, that takes User input
- Game Over screen with retry option

![App Screenshot](https://www.simpleimageresizer.com/_uploads/photos/fd48d8b6/gameop2_99.png)

### Future Features

- Implement items that contain various info, like letters and notes
- Implement number codes needed to pass a scenario
- More advanced ASCII-Artwork





## Testing

I have manually tested the project with these methods

- Run the code trough a PEP8 linter to check that everything works
- Given invalid inputs like number and other keys in the choice options
- Tested both in my local terminal and on Heroku


### Bugs

- No bugs where found during the making or testing of the project


### Validator Testing

- PEP8

 Some minor errors found like trailing whitespaces and so on.
 Nothing that disturbs the performance of the game. 
## Deployment

The project was deployed by first Creating an App on Heroku.com then connecting it
to GitHub.

- Create a new Heroku App
- Add a new Config Var with an port
- include the buildbacks `Python` and `NodeJS`
- Connect the Heroku App to the repository
- Click on **Deploy**


## Credits

- [ASCII-Art Generator](https://patorjk.com/software/taag/) For helping me generate the logo and game-over screen

- [Colored Text in Python](https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python) For guiding me on how to add colors to console text.