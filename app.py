#!/usr/bin/env python3

# Author: Felixity1917@github
# This program has been licensed under the clauses of GNU Public License v3.
# The source code of this program is available at https://github.com/felixity1917/tekstrakontludo
# Version: 1.0 Stable (2024-10-30)

# VIT Registration Number: 24BCE0981

# Libraries
import time;
import sys;
import shutil;
import random;

# Variables
en_hp = 50;

# Function to print text with typewriter effect.
# Contains switch to modify text with modified center function.
def twrfx(msg,swch=1,dlay=0.03):
    if swch == 1:
        msg = cwrs(msg);
    for cr in msg:
        if cr != ' ':
            sys.stdout.write(cr);
            sys.stdout.flush();
            time.sleep(dlay);
        else:
            sys.stdout.write(' ');
            sys.stdout.flush();
            # time.sleep(dlay);
    print();

# Function to print each line of text using typewriter function.
# Contains switch(1) to add spacing between each line.
# Contains switch(2) which corresponds to switch(1) of typewriter function.
def prtm(mdic,swch1=1,swch2=1):
    for i in range(len(mdic)):
        if swch2 == 1:
            twrfx(mdic[i],1);
        else:
            twrfx(mdic[i],0);
        if swch1 == 1:
            print();
        else:
            continue;

# Modified center() function to center text according to screen(terminal) size.
# Additionally strips the spaces from the right side.
def cwrs(txt):
    ttcl, _ = shutil.get_terminal_size();
    txt_len = len(txt);

    if txt_len < ttcl:
        lspc = (ttcl - txt_len) // 2;
    else:
        lspc = 0;

    ctrd_text = ' ' * lspc + txt;
    return ctrd_text.rstrip();

# Function to assign variables according to player class chosen.
def itcn(plc):
    plcn = 0;
    while True:
        if plc == '1':
            plc = 'Swordsman';
            plcn = 1;
            pl_hp = 140;
            break;
        elif plc == '2':
            plc = 'Archer';
            plcn = 2;
            pl_hp = 100;
            break;
        elif plc == '3':
            plc = 'Mage';
            plcn = 3;
            pl_hp = 40;
            break;
        else:
            twrfx('Invalid input. Please try again.');
            plc = input('»»» ');
    return plc, plcn, pl_hp;

# Prototype function to check for player's HP.
def death_fn():
    if pl_hp <= 0:
        death_txt = {
            0 : 'You fought brave and hard.',
            1 : 'But alas, you\'ve bled too much.',
            2 : 'Your vision fades and so does your life...'
        };
        prtm(death_txt,0);
        print();
        rtry_c_fn();

# Attack function.
def attack_en(plcn):
    global pl_hp, en_hp;
    if plcn == 1: # Swordsman
        dmg = 5; # Low Attack
        poh = 90; # High Probability of Hit (%)
    elif plcn == 2: # Archer
        dmg = 10; # Moderate attack
        poh = 60; # Low PoH
    elif plcn == 3: # Mage
        dmg = 20; # High attack
        poh = 75; # Moderate PoH
    else:
        twrfx('Unknown Error. Please contact your local technician.')
        exit();

    if random.randint(1,100) <= poh:
        twrfx(f'Attack successful. You dealt a damage of {dmg}.');
        en_hp -= dmg;
    else:
        twrfx('You missed.');

    if en_hp <= 0:
        victory_fn();
        return;
    elif pl_hp <= 0:
        death_fn();
        return

    en_poh = 60;
    if random.randint(1,100) > en_poh:
        en_dmg = random.randint(1,20);
        twrfx(f'The enemy deals a damage of {en_dmg}.');
        pl_hp -= en_dmg;
    else:
        twrfx('The enemy missed.');

    twrfx(f'Your HP: {pl_hp}');
    twrfx(f'Enemy\'s HP: {en_hp}');
    print();

# Defend self function.

def defend_self(plcn):
    global pl_hp, en_hp;
    if plcn == 1:  # Swordsman
        heal_amt = 10;  # Low healing
    elif plcn == 2:  # Archer
        heal_amt = 25;  # Moderate healing
    elif plcn == 3:  # Mage
        heal_amt = 45;   # High healing
    else:
        twrfx("Unknown Error. Please contact your local technician");
        exit();

    pl_hp += heal_amt;
    en_hp += 45;  # Enemy heals by a fixed amount

    twrfx(f"You healed by {heal_amt} HP.");
    twrfx(f"The enemy also healed by 45 HP.");

    twrfx(f'Your HP: {pl_hp}');
    twrfx(f'Enemy\'s HP: {en_hp}');
    print();

# Victory function.

def victory_fn():
    victory_txt = {
        0 : 'You won.',
        1 : 'By defeating your first foes in this brutal battle,',
        2 : 'You\'ve shown that you truly are a champion of the realm.',
        3 : 'May you have a Victorious legacy.',
        4 : '.           .            .             .              .',
        5 : 'Thanks for playing.'
    };
    prtm(victory_txt);
    exit();

# Function that executes when you choose Choice 1 (Run).
def str1_ch1_fn():
    str1_p1_txt = {
        0 : 'You run as fast as you can. But alas, it seems God had some other plans...',
        1 : 'You trip on a small rock and fall head first onto a marble slab',
        2 : 'Oh the fall was too great and too quick.',
        3 : 'And the story of our hero and come to an end as quickly as it had started.'
    };
    prtm(str1_p1_txt,0);
    rtry_fn();

# Function that runs when you choose Choice 2 (Fight).
def str1_ch2_fn():
    global p2_c1_ch;
    str1_p2_txt = {
        0 : 'Quickly, you analyze the 3 men standing in front of you.',
        1 : 'You pull out your weapon and instantly decapitate the man right in front of you and surprise them.',
        2 : 'One of the bandits flees in torment while the other brandishes his sword quickly while trembling.',
        3 : 'This is your first real battle for your life.',
        4 : 'This will prove if you are fit to be a warrior and hero of this realm.',
        5 : 'FIGHT'
    };
    prtm(str1_p2_txt,0);
    print();
    str1_p2_c1_txt = {
        0 : 'The Bandit is readying for his next move.',
        1 : 'Quick, choose your next move.',
        2 : '1 - Attack the bandit',
        3 : '2 - Defend yourself',
        4 : '3 - Run away',
        5 : '4 - Negotiate a Trade Deal',
        6 : 'Enter 1 or 2 or 3 or 4'
    };
    prtm(str1_p2_c1_txt,0);
    p2_c1_ch = input('»»» ');
    while True:
        if p2_c1_ch == '1':
            str1_ch2_p1_fn();
        elif p2_c1_ch == '2':
            str1_ch2_p2_fn();
        elif p2_c1_ch == '3':
            str1_ch2_p3_fn();
        elif p2_c1_ch == '4':
            str1_ch2_p4_fn();
        else:
            twrfx('Incorrect Input. Try Again.');
            p2_c1_ch = input('»»» ');

# Function that is executed when you choose Choice 1 (Slash your sword at the bandit) of Choice 2 (Fight)
def str1_ch2_p1_fn():
    global p2_c1_ch;
    p2_c1_ch1_txt = {
        0 : 'An exchange of violence ensues',
        1 : '...',
        2 : '...',
        3 : '...'
    };
    prtm(p2_c1_ch1_txt,0);
    print();
    attack_en(plcn);
    prtm(str1_c_rtry_txt,0);
    p2_c1_ch = input('»»» ');

# Function that is executed when you choose Choice 2 (Defend yourself) of Choice 2 (Fight).
def str1_ch2_p2_fn():
    global p2_c1_ch;
    p2_c1_ch2_txt = {
        0 : 'You parry the enemy\'s attack and heal a little.'
    };
    prtm(p2_c1_ch2_txt);
    defend_self(plcn);
    prtm(str1_c_rtry_txt,0);
    p2_c1_ch = input('»»» ');

# Function that is executed when you choose Choice 3 (Run away) of Choice 2 (Fight).
def str1_ch2_p3_fn():
    p2_c1_ch3_txt = {
        0 : 'As you turn around to run away, you get impaled by the enemy\'s sword.',
        1 : 'It seems, maybe you weren\'t destined to be the hero of the realm.',
        2 : 'Or maybe you can turn back time and we will all forget this mockery of chivalry.'
    };
    prtm(p2_c1_ch3_txt,0);
    rtry_c_fn();

# Function that is executed when you choose Choice 4 (Negotiate a Trade Deal) of Choice 2 (Fight).
def str1_ch2_p4_fn():
    p2_c1_ch4_txt = {
        0 : 'Well, while you were conjuring these meticulous trade dealings.',
        1 : 'You get impaled by the enemy\'s sword',
        2 : 'I am not sure whether you are in the right game.',
        3 : 'So I shall remind you that this indeed is a Combat game.'
    };
    prtm(p2_c1_ch4_txt,0);
    rtry_c_fn();

# Function that is executed when you choose Choice 3 (Negotiate a Trade Deal)
def str1_ch3_fn():
    str1_p3_txt = {
        0 : '"Get a load of this chum, lads." says one of the bandits.',
        1 : 'They want us to "Negotiate" for a piece of bread. What a joke. Seize them, lads!',
        2 : 'In the ensuing scuffle, you get stabbed in the back while you were developing intricate ideas of Trade....',
        3 : '..... with bandits.'
    };
    prtm(str1_p3_txt,0);
    rtry_fn();

# Function that is executed each time there is a Game Over.
def rtry_fn():
    global str1_ch;
    prtm(rtry_txt,0);
    rtry_ch = input('»»» ');
    while True:
        if rtry_ch == '1':
            prtm(str1_rtry_txt,0);
            str1_ch = input('»»» ');
            break;
        elif rtry_ch == '0':
            twrfx(f'Then farewell, {plm}. We might meet again in the future if our destinies intersect.');
            exit();
        else:
            twrfx('Incorrect input. Try again.');
            rtry_ch = input('»»» ');

# Previous function but only executed for segments where there is actual combat.
def rtry_c_fn():
    global p2_c1_ch;
    prtm(rtry_txt,0);
    rtry_ch = input('»»» ');
    while True:
        if rtry_ch == '1':
            prtm(str1_c_rtry_txt,0);
            p2_c1_ch = input('»»» ');
            break;
        elif rtry_ch == '0':
            twrfx(f'Then farewell, {plm}. We might meet again in the future if our destinies intersect.');
            exit();
        else:
            twrfx('Incorrect input. Try again.');
            rtry_ch = input('»»» ');


# ------ GAME START ------ #

init_txt = {
    0 : 'Welcome to Tekstrakontludo, a short choices-based story game in cli mode written in Python.',
    1 : 'Tekstrakontludo is an Esperanto word that means "A Text Story Game".',
};
prtm(init_txt);

twrfx('Please enter your name.');
plm = input('»»» ');

print();

plcc_txt = {
    0 : 'Please choose wisely, one of the following 3 classes of warriors you would like to be',
    1 : '1 - Swordsman',
    2 : '2 - Archer',
    3 : '3 - Mage',
    4 : 'Enter 1 or 2 or 3',
};
prtm(plcc_txt,0);
plc = input('»»» ');
plc, plcn, pl_hp = itcn(plc);

print();

entr_txt = {
    0 : f'You\'ve chosen {plc}.',
    1 : f'And hence begins the story of {plm}, a novice {plc} born into the hallow world of Gottheim - God\'s own home.',
};
prtm(entr_txt);

str1_txt = {
    0 : 'In Gottheim, you live a life of poverty and impoverishment. Contrary to its heraldry, its rulers are corrupt and vile.',
    1 : 'One fine day, you are walking down an alleyway, bringing to home your daily ration provided by the local church.',
    2 : 'When you get surrounded by some shady folks.',
    3 : '"Give that bread to me if you value your life.", says one of the men. What do you do?',
    4 : '1 - Run',
    5 : '2 - Fight',
    6 : '3 - Negotiate a Trade Deal',
    7 : 'Enter 1 or 2 or 3'
};
str1_rtry_txt = {
    0 : '...',
    1 : '"Give that bread to me if you value your life.", says one of the men. What do you do?',
    2 : '1 - Run',
    3 : '2 - Fight',
    4 : '3 - Negotiate a Trade Deal',
    5 : 'Enter 1 or 2 or 3'
};
prtm(str1_txt,0);

global str1_ch;
str1_ch = input('»»» ');

rtry_txt = {
    0 : 'Retry?',
    1 : '1 - Yes',
    2 : '0 - No',
    3 : 'Enter 1 or 0'
};

str1_c_rtry_txt = {
    0 : '...',
    1 : 'The Bandit is readying for his next move.',
    2 : 'Quick, choose your next move.',
    3 : '1 - Attack the bandit',
    4 : '2 - Defend yourself',
    5 : '3 - Run away',
    6 : '4 - Negotiate a Trade Deal',
    7 : 'Enter 1 or 2 or 3 or 4'
};

while True:
    if str1_ch == '1':
        str1_ch1_fn();
    elif str1_ch == '2':
        str1_ch2_fn();
    elif str1_ch == '3':
        str1_ch3_fn();
    else:
        twrfx('Incorrect Input. Try again.');
        str1_ch = input('»»» ');
