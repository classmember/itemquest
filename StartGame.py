#!/usr/bin/env python3
""" game desc"""

from Menu import menu
from MainStory import main_story
from PlayerCharacter import PlayerCharacter


def init():
    """Initializes all data needed for game"""


def game_loop():
    """Game loop"""
    exit_status = False
    while exit_status is False:
        main_menu = ("Start", "Credits", "Exit")
        selection = menu(main_menu)
        if selection is 1:
            player = PlayerCharacter()
            player.race_select()
            player.confirm_setup()
            main_story(player)
            exit_status = True
        if selection is 2:
            print ("This game was developed by Brian Kordek " +
                   "with generous assistance from Kolby Heacock.")
        if selection is 3:
            exit_status = True


def clean_up():
    """Clean up things"""
    pass


def main():
    """the application's starting point"""
    init()
    game_loop()
    clean_up()


if __name__ == '__main__':
    main()
