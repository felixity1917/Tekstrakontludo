# Tekstrakontludo
Tekstrakontludo is my first take on a short Choices-Driven RPG in Cli mode.

This is also my very first game that I have made on my own.

Tekstrakontludo is an Esperanto word which literally means 'A Text Story Game'.

(This was made as an assignment project in my University (VIT). VIT Registration Number: 24BCE0981)

# Running the game

1. Make sure you have Python installed on your system. If it's not there then please refer online sources on how to install Python on your system.
2. Clone this repository.
``` sh
git clone https://github.com/felixity1917/Tekstrakontludo.git
```
3. Execute the following commands.
``` sh
cd Tekstrakontludo
python app.py
```

Alternatively you can test it with any suitable IDE which supports Python.

# Documentation

The explanation will be delineated into 4 categories, The Modules, The Static String Library, The Functions and The Main Process. In the same order as their declaration in the code itself.

## The Modules

I have imported the following modules
- time
- sys
- shutil
- random

These come pre-packaged with Python and do not need to be installed using pip seperately.

The `time` module has been used to generate a delay between each character's print in the `typewriter_effect()` function.

The `sys` module has been used to print out the character onto the terminal screen in the `typewriter_effect()` function.

The `shutil` module has been used to fetch the terminal window's screen size as columns and rows in the `center_modified()` function.

The `random` module has been used to generate class based damage, probability of hit and hitpoints of the player in the related functions.

## The Static String Library

This section includes all the static strings containing all dialogues which will be printed during the gameplay. Each instance is a dictionary of a set of strings. The strings in a dictionary are printed in order whenever they are called by either the `typewriter_effect()` or `print_modified()` functions.

## The Functions

This section includes all the declared functions which have been used in the game.

### `typewriter_effect()`

This function accepts 3 arguments, `msg`, `center_switch` and `delay`, where the default values for `center_switch` and `delay` are `1` and `0.03` respectively. The `center_switch` formats the provided `msg` with the `center_modified()` function when it is equal to `1`. The function prints each character in `msg` with a time delay to mimic a typewriter effect while eliminating any delay for printing empty characters (`' '`).

### `print_modified()`

This function accepts 3 arguments, `msg_dictionary`, `line_break_switch`, `center_switch`, where the default values for `line_break_switch` and `center_switch` are `1` and `1` respectively. The `center_switch` shares the same functionality as the switch in the `typewriter_effect()` function. The `line_break_switch` prints an empty line after the main dialogue when equal to `1`.

### `center_modified()`

This function fetches and stores the number of columns of the terminal screen and the length of each string `msg`. It calculates the number of spaces to be generated to the left of the `msg` so that it is centered on the terminal screen according to its size. And doesn't generate any spacing when the `msg` is longer than the terminal width.

### `class_properties_assignment()`

This function accepts a single argument which is `chosen_class`. It assigns the player their `player_class`, `player_class_number` and `player_hp` according to their choice.

### `attack_enemy()`

This function accepts a single argument which is `player_class_number`. It assigns the `damage` and `probability_of_hit` according to the `player_class_number`. The `probability_of_hit` decides whether the next attack will hit or miss and if it hits, the enemy will get a reduction in `enemy_hp` equivalent to `damage`. The same procedure takes place on the enemy's side as well using the variables `enemy_probability_of_hit` and `enemy_damage`. If the `enemy_hp` goes to `0` or below, the function breaks any further calculation and calls `victory_function()` and if the `player_hp` goes to `0` or below, the function breaks any further calculation and calls `death_function()`. If there is possibility of continuity of the battle, then it ends after printing out `player_hp` and `enemy_hp`.

### `defend_self()`

This function accepts a single argument which is `player_class_number`. It assigns the `heal_amount` according to the `player_class_number`. Each time it is called. It increases the value of `player_hp` by `heal_amount`. and `enemy_hp` by `45`. It then notifies the player about the value changes and prints the `player_hp` and `enemy_hp`.

### Story Path Functions

The `story_*()` functions control how the story unfolds according to the user's provided choices. They call the appropriate functions according to the user's provided input after each scene dialogue.

### `retry_function()`

This function is executed on user death and gives the user a choice to retry the game and provides them the last path they were on so that they may revise their choice.

### `retry_combat_function()`

This function shares its functionality with the `retry_function()` but with a few variable changes and is executed on user death during the combat scenes.

### `victory_function()`

As it's name implies. This function is executed on the player's epic win. It prints a `victory_msg` and ends the game.

### `death_function()`

Similar to the `victory_function()`. This function is executed on user death during the combat scene. It prints a `death_msg` and ends the game.

## Main Process

The Main Process consists of a linear order of functions to be called to generate the story properly and consistently from beginning to finish. It accepts the `player_name` and `player_class` in the beginning of the game.
