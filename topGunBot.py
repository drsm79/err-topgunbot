#!/usr/bin/env python


"""A bot which will respond to various TOP GUN character name commands and
mentions and respond with a random line spoken by that character in the film.
"""

import logging
from random import choice
from errbot import BotPlugin, botcmd
from topGun import TopGun


class TopGunBot(BotPlugin):
    def activate(self):
        super(TopGunBot, self).activate()
        self.topgun_script = TopGun()
        logging.info(self.topgun_script.CHARACTERS.keys())

    @botcmd(split_args_with=' ')
    def topgun(self, mess, args):
        character = args[0]
        if character not in self.topgun_script.CHARACTERS.keys():
            character = choice(self.topgun_script.CHARACTERS.keys())
        return '%s: "%s"' % (
            character, self.topgun_script.get_random(character)
        )
