#!/usr/bin/env python3

# Author: Felixity1917@github
# This program has been licensed under the clauses of GNU Public License v3.
# The source code of this program is available at https://github.com/felixity1917/tekstrakontludo
# Version: 1.0-1 Stable (2024-11-01)

# VIT Registration Number: 24BCE0981

# ------ Imported Libraries ------
import time;
import sys;
import shutil;
import random;

# ------ Init Variables ------
player_hp = 100;
enemy_hp = 50;
player_name = 'Champion';
player_class = 'Champion';
player_class_number = 0;

# ------ Static String Dictionaries ------

init_msg = {
    0 : 'Welcome to Tekstrakontludo, a short choices-based story game in cli mode written in Python.',
    1 : 'Tekstrakontludo is an Esperanto word that means "A Text Story Game".',
};

player_class_selection_msg = {
    0 : 'Please choose wisely, one of the following 3 classes of warriors you would like to be',
    1 : '1 - Swordsman',
    2 : '2 - Archer',
    3 : '3 - Mage',
    4 : 'Enter 1 or 2 or 3',
};

story_msg = {
    0 : 'In Gottheim, you live a life of poverty and impoverishment. Contrary to its heraldry, its rulers are corrupt and vile.',
    1 : 'One fine day, you are walking down an alleyway, bringing to home your daily ration provided by the local church.',
    2 : 'When you get surrounded by some shady folks.',
    3 : '"Give that bread to me if you value your life.", says one of the men. What do you do?',
    4 : '1 - Run',
    5 : '2 - Fight',
    6 : '3 - Negotiate a Trade Deal',
    7 : 'Enter 1 or 2 or 3'
};

story_retry_msg = {
    0 : '...',
    1 : '"Give that bread to me if you value your life.", says one of the men. What do you do?',
    2 : '1 - Run',
    3 : '2 - Fight',
    4 : '3 - Negotiate a Trade Deal',
    5 : 'Enter 1 or 2 or 3'
};

retry_msg = {
    0 : 'Retry?',
    1 : '1 - Yes',
    2 : '0 - No',
    3 : 'Enter 1 or 0'
};

story_combat_retry_msg = {
    0 : '...',
    1 : 'The Bandit is readying for his next move.',
    2 : 'Quick, choose your next move.',
    3 : '1 - Attack the bandit',
    4 : '2 - Defend yourself',
    5 : '3 - Run away',
    6 : '4 - Negotiate a Trade Deal',
    7 : 'Enter 1 or 2 or 3 or 4'
};

story_path_1_msg = {
    0 : 'You run as fast as you can. But alas, it seems God had some other plans...',
    1 : 'You trip on a small rock and fall head first onto a marble slab',
    2 : 'Oh the fall was too great and too quick.',
    3 : 'And the story of our hero and come to an end as quickly as it had started.'
};

story_path_2_msg = {
    0 : 'Quickly, you analyze the 3 men standing in front of you.',
    1 : 'You pull out your weapon and instantly decapitate the man right in front of you and surprise them.',
    2 : 'One of the bandits flees in torment while the other brandishes his sword quickly while trembling.',
    3 : 'This is your first real battle for your life.',
    4 : 'This will prove if you are fit to be a warrior and hero of this realm.',
    5 : 'FIGHT'
};

story_path_2_combat_msg = {
    0 : 'The Bandit is readying for his next move.',
    1 : 'Quick, choose your next move.',
    2 : '1 - Attack the bandit',
    3 : '2 - Defend yourself',
    4 : '3 - Run away',
    5 : '4 - Negotiate a Trade Deal',
    6 : 'Enter 1 or 2 or 3 or 4'
};

story_path_2_choice_1_msg = {
    0 : 'An exchange of violence ensues',
    1 : '...',
    2 : '...',
    3 : '...'
};

story_path_2_choice_2_msg = {
    0 : 'You parry the enemy\'s attack and heal a little.'
};

story_path_2_choice_3_msg = {
    0 : 'As you turn around to run away, you get impaled by the enemy\'s sword.',
    1 : 'It seems, maybe you weren\'t destined to be the hero of the realm.',
    2 : 'Or maybe you can turn back time and we will all forget this mockery of chivalry.'
};

story_path_2_choice_4_msg = {
    0 : 'Well, while you were conjuring these meticulous trade dealings.',
    1 : 'You get impaled by the enemy\'s sword',
    2 : 'I am not sure whether you are in the right game.',
    3 : 'So I shall remind you that this indeed is a Combat game.'
};

story_path_3_msg = {
    0 : '"Get a load of this chum, lads." says one of the bandits.',
    1 : 'They want us to "Negotiate" for a piece of bread. What a joke. Seize them, lads!',
    2 : 'In the ensuing scuffle, you get stabbed in the back while you were developing intricate ideas of Trade....',
    3 : '..... with bandits.'
};

# ------ Functions ------

# Function to print text with typewriter effect.
# Contains switch to modify text with modified center function.
def typewriter_effect(msg,center_switch=1,delay=0.03):
    if center_switch == 1:
        msg = center_modified(msg);
    for character in msg:
        if character != ' ':
            sys.stdout.write(character);
            sys.stdout.flush();
            time.sleep(delay);
        else:
            sys.stdout.write(' ');
            sys.stdout.flush();
            # time.sleep(delay); # Uncomment to print empty spaces with effect as well.
    print();

# Function to print each line of text using typewriter function.
# Contains line_break_switch to add a line break between each line.
# Contains center_switch which corresponds to the typewriter function's switch with the same name.
def print_modified(msg_dictionary,line_break_switch=1,center_switch=1):
    for i in range(len(msg_dictionary)):
        if center_switch == 1:
            typewriter_effect(msg_dictionary[i],1);
        else:
            typewriter_effect(msg_dictionary[i],0);
        if line_break_switch == 1:
            print();
        else:
            continue;

# Modified center() function to center text according to screen(terminal) size.
# Additionally strips the spaces from the right side.
def center_modified(msg):
    tty_columns, _ = shutil.get_terminal_size();
    msg_length = len(msg);

    if msg_length < tty_columns:
        lspc = (tty_columns - msg_length) // 2;
    else:
        lspc = 0;

    ctrd_text = ' ' * lspc + msg;
    return ctrd_text.rstrip();

# Function to assign variables according to player class chosen.
def class_properties_assignment(chosen_class):
    global player_class, player_class_number, player_hp;
    while True:
        if chosen_class == '1':
            player_class = 'Swordsman';
            player_class_number = 1;
            player_hp = 140;
            break;
        elif chosen_class == '2':
            player_class = 'Archer';
            player_class_number = 2;
            player_hp = 100;
            break;
        elif chosen_class == '3':
            player_class = 'Mage';
            player_class_number = 3;
            player_hp = 40;
            break;
        else:
            typewriter_effect('Invalid input. Please try again.');
            chosen_class = input('»»» ');

# Attack function.
def attack_enemy(player_class_number):
    global player_hp, enemy_hp;
    if player_class_number == 1: # Swordsman
        damage = 5; # Low Attack
        probability_of_hit = 90; # High Probability of Hit (%)
    elif player_class_number == 2: # Archer
        damage = 10; # Moderate attack
        probability_of_hit = 60; # Low Probability of Hit (%)
    elif player_class_number == 3: # Mage
        damage = 20; # High attack
        probability_of_hit = 75; # Moderate Probability of Hit (%)
    else:
        typewriter_effect('Unknown Error. Please contact your local technician.')
        exit();
    if random.randint(1,100) <= probability_of_hit:
        typewriter_effect(f'Attack successful. You dealt a damage of {damage}.');
        enemy_hp -= damage;
    else:
        typewriter_effect('You missed.');
    if enemy_hp <= 0:
        victory_function();
        return;
    elif player_hp <= 0:
        death_function();
        return
    en_probability_of_hit = 60;
    if random.randint(1,100) > en_probability_of_hit:
        enemy_damage = random.randint(1,20);
        typewriter_effect(f'The enemy deals a damage of {enemy_damage}.');
        player_hp -= enemy_damage;
    else:
        typewriter_effect('The enemy missed.');
    typewriter_effect(f'Your HP: {player_hp}');
    typewriter_effect(f'Enemy\'s HP: {enemy_hp}');
    print();

# Defend self function.
def defend_self(player_class_number):
    global player_hp, enemy_hp;
    if player_class_number == 1:  # Swordsman
        heal_amount = 10;  # Low healing
    elif player_class_number == 2:  # Archer
        heal_amount = 25;  # Moderate healing
    elif player_class_number == 3:  # Mage
        heal_amount = 45;   # High healing
    else:
        typewriter_effect("Unknown Error. Please contact your local technician");
        exit();
    player_hp += heal_amount;
    enemy_hp += 45;  # Enemy heals by a fixed amount
    typewriter_effect(f"You healed by {heal_amount} HP.");
    typewriter_effect(f"The enemy also healed by 45 HP.");
    typewriter_effect(f'Your HP: {player_hp}');
    typewriter_effect(f'Enemy\'s HP: {enemy_hp}');
    print();

# Function that executes when you choose Choice 1 (Run).
def story_choice_1_fn():
    print_modified(story_path_1_msg,0);
    retry_function();

# Function that runs when you choose Choice 2 (Fight).
def story_choice_2_fn():
    global story_path_2_combat_choice;
    print_modified(story_path_2_msg,0);
    print();
    print_modified(story_path_2_combat_msg,0);
    story_path_2_combat_choice = input('»»» ');
    while True:
        if story_path_2_combat_choice == '1':
            story_path_2_choice_1_function();
        elif story_path_2_combat_choice == '2':
            story_path_2_choice_2_function();
        elif story_path_2_combat_choice == '3':
            story_path_2_choice_3_function();
        elif story_path_2_combat_choice == '4':
            story_path_2_choice_4_function();
        else:
            typewriter_effect('Incorrect Input. Try Again.');
            story_path_2_combat_choice = input('»»» ');

# Function that is executed when you choose Choice 1 (Attack the bandit) of Choice 2 (Fight)
def story_path_2_choice_1_function():
    global story_path_2_combat_choice;
    print_modified(story_path_2_choice_1_msg,0);
    print();
    attack_enemy(player_class_number);
    print_modified(story_combat_retry_msg,0);
    story_path_2_combat_choice = input('»»» ');

# Function that is executed when you choose Choice 2 (Defend yourself) of Choice 2 (Fight).
def story_path_2_choice_2_function():
    global story_path_2_combat_choice;
    print_modified(story_path_2_choice_2_msg);
    defend_self(player_class_number);
    print_modified(story_combat_retry_msg,0);
    story_path_2_combat_choice = input('»»» ');

# Function that is executed when you choose Choice 3 (Run away) of Choice 2 (Fight).
def story_path_2_choice_3_function():
    print_modified(story_path_2_choice_3_msg,0);
    retry_combat_function();

# Function that is executed when you choose Choice 4 (Negotiate a Trade Deal) of Choice 2 (Fight).
def story_path_2_choice_4_function():
    print_modified(story_path_2_choice_4_msg,0);
    retry_combat_function();

# Function that is executed when you choose Choice 3 (Negotiate a Trade Deal)
def story_choice_3_fn():
    print_modified(story_path_3_msg,0);
    retry_function();

# Function that is executed each time there is a Game Over.
def retry_function():
    global story_choice;
    print_modified(retry_msg,0);
    retry_choice = input('»»» ');
    while True:
        if retry_choice == '1':
            print_modified(story_retry_msg,0);
            story_choice = input('»»» ');
            break;
        elif retry_choice == '0':
            typewriter_effect(f'Then farewell, {player_name}. We might meet again in the future if our destinies intersect.');
            exit();
        else:
            typewriter_effect('Incorrect input. Try again.');
            retry_choice = input('»»» ');

# Previous function but only executed for segments where there is actual combat.
def retry_combat_function():
    global story_path_2_combat_choice;
    print_modified(retry_msg,0);
    retry_choice = input('»»» ');
    while True:
        if retry_choice == '1':
            print_modified(story_combat_retry_msg,0);
            story_path_2_combat_choice = input('»»» ');
            break;
        elif retry_choice == '0':
            typewriter_effect(f'Then farewell, {player_name}. We might meet again in the future if our destinies intersect.');
            exit();
        else:
            typewriter_effect('Incorrect input. Try again.');
            retry_choice = input('»»» ');

# Victory function.
def victory_function():
    victory_msg = {
        0 : 'You won.',
        1 : 'By defeating your first foes in this brutal battle,',
        2 : 'You\'ve shown that you truly are a champion of the realm.',
        3 : 'May you have a Victorious legacy.',
        4 : '.           .            .             .              .',
        5 : 'Thanks for playing.'
    };
    print_modified(victory_msg);
    exit();

# Prototype function to check for player's HP.
def death_function():
    if player_hp <= 0:
        death_msg = {
            0 : 'You fought brave and hard.',
            1 : 'But alas, you\'ve bled too much.',
            2 : 'Your vision fades and so does your life...'
        };
        print_modified(death_msg,0);
        print();
        retry_combat_function();

# ------ Main Process ------

print_modified(init_msg);
typewriter_effect('Please enter your name.');
player_name = input('»»» ');
print();
print_modified(player_class_selection_msg,0);
player_class = input('»»» ');
class_properties_assignment(player_class);
entry_msg = {
    0 : f'You\'ve chosen {player_class}.',
    1 : f'And hence begins the story of {player_name}, a novice {player_class} born into the hallow world of Gottheim - God\'s own home.',
};
print_modified(entry_msg);
print_modified(story_msg,0);
story_choice = input('»»» ');
while True:
    if story_choice == '1':
        story_choice_1_fn();
    elif story_choice == '2':
        story_choice_2_fn();
    elif story_choice == '3':
        story_choice_3_fn();
    else:
        typewriter_effect('Incorrect Input. Try again.');
        story_choice = input('»»» ');

# ------ EOF ------
