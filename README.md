# Python 401d1818
## Labs(06-09): Ten Thousand
### Authors: 

## Lab: 06
### Setup
* Work in teams to build a command line version of the dice game Ten Thousand by expanding your understanding of Python standard library.

### Feature Tasks and Requirements
Create a project named `ten-thousand`.
Today is all about tackling the highest risk and/or highest priority features - **scoring, dice rolling and banking of points**.
  * Define a `GameLogic` class in `ten_thousand/game_logic.py` file.
  * Handle calculating score for dice roll
    * Add `calculate_score` static method to GameLogic class.
    * The input to `calculate_score` is a tuple of integers that represent a dice roll.
    * The output from `calculate_score` is an integer representing the roll’s score according to **rules of game**.
    
  * Handle rolling dice
    * Add `roll_dice` static method to GameLogic class.
    * The input to `roll_dice` is an integer between 1 and 6.
    * The output of `roll_dice` is a tuple with random values between 1 and 6.
    * The length of tuple must match the argument given to `roll_dice` method.
  * Handle banking points
    * Define a `Banker` class
    * Add a `shelf` instance method
      * Input to `shelf` is the amount of points (integer) to add to shelf.
      * `shelf` should temporarily store *unbanked* points.
  * Add a `bank` instance method
    * `bank` should add any points on the *shelf* to total and reset shelf to 0.
    * `bank` output should be the amount of points added to total from shelf.
  * Add a `clear_shelf` instance method
    * `clear_shelf` should remove all unbanked points.

### Implementation Notes
  * Review [rules of game](https://en.wikipedia.org/wiki/Dice_10000)
  * Play [game online](http://www.playonlinedicegames.com/farkle)

### User Acceptance Tests:
- [Starter tests](https://github.com/codefellows/seattle-python-401d18/blob/main/class-06/demo/parametrized-tests/tests/test_game_logic.py) will be provided that cover cases listed below
  - All tests must pass as written (additional tests are allowed)

### Testing:

#### Roll Dice:
When rolling 1 to 6 dice ensure:
- A sequence of correct length is returned
- Each item in sequence is an integer with value between 1 and 6

#### Calculate Score:
* zilch - roll with no scoring dice should return 0
* ones - rolls with various number of 1s should return correct score
* twos - rolls with various number of 2s should return correct score
* threes - rolls with various number of 3s should return correct score
* fours - rolls with various number of 4s should return correct score
* fives - rolls with various number of 5s should return correct score
* sixes - rolls with various number of 6s should return correct score
* straight - 1,2,3,4,5,6 should return correct score
* three_pairs - 3 pairs should return correct score
* two_trios - 2 sets of 3 should return correct score
* leftover_ones - 1s not used in set of 3 (or greater) should return correct score
* leftover_fives - 5s not used in set of 3 (or greater) should return correct score

#### Banker:
* shelf
  * should properly track unbanked points
* bank
  * should properly add unbanked points to total and return the deposited amount
* clear_shelf
  * should remove any unbanked points, resetting to zero.
  * should not affect previously banked points

### Stretch:
- Research `parametrized tests in PyTest`
- Research `Behavior Driven Development`

<!--- 
## Lab: 07
Extend Ten Thousand game started in previous class to get the game in playable state.

### Feature Tasks and Requirements
* Application should implement all features from previous version
* Application should simulate rolling between 1 and 6 dice
* Application should allow user to set aside dice each roll
* Application should allow “banking” current score or rolling again.
* Application should keep track of total score
* Application should keep track of current round
* Application should have automated tests to ensure proper operation

### User Acceptance Tests
* Starter code contains acceptance tests in the form of “simulation” files.
  * E.g. tests/version_1/quitter.sim.txt
* These simulation files are used in concert with tests/flo.py to examine actual vs. expected output.
* Tests for today are provided.
  * **NOTE**: Feel free to add tests, but you are required to pass all existing tests.
* The tests are the official documentation of the features for the day.

## Lab: 08
Shore up the core functionality of game by allowing users to set aside scoring dice and continuing their turn.
Then handle cheaters and/or confused players who are skirting the rules.

### Feature Tasks and Requirements
* Application should implement features from versions 1 and 2
* Should handle setting aside scoring dice and continuing turn with remaining dice.
* Should handle when cheating occurs.
  * Or just typos.
  * E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
* Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
* Handle zilch
  * No points for round, and round is over

### Stretch Goals
* Identify features to add and propose idea to client.
* Identify gaps in current test suite and add tests to expose bugs.

## Lab: 09
Add an AI bot to play the game.

### Feature Tasks and Requirements
* Create an AI Bot to play Ten Thousand
  * The only method available for use from Game class is `play`.
  * All static methods of `GameLogic` class are available.
  * All other interactions with game can take place **ONLY** via the I/O features of the game.
    * In other words, via injectable `print` and `input` functionality.
    * It is FORBIDDEN to inject a custom `roller` function into Game class.
* Copy bots.py to your project.
  * Place it at root of project, at same level as `pyproject.toml`
* Your Bot class should be added to `bots.py` file with name of your choosing replacing `YourBot`.
  * **NOTE** the code for `BaseBot` class is supplied for reference, but your custom code will be in the overridden `_roll_bank_or_quit` and `_enter_dice` methods.
* User should be able to see your bot play by executing `bots.py` from terminal.
* Application should implement features from previous classes
--->