#!/usr/bin/env python


"""A bot which will respond to various TOP GUN character name commands and
mentions and respond with a random line spoken by that character in the film.
"""

from errbot import BotPlugin, botcmd
from errbot.utils import get_sender_username
import config
import logging
from random import choice
from topGun import TopGun


class TopGunBot(BotPlugin):
    def activate(self):
        super(TopGunBot, self).activate()
        self.topgun_script = TopGun()
        logging.info(self.topgun_script.CHARACTERS.keys())

    @botcmd
    def topgun(self, conn, mess):
        character = choice(self.topgun_script.CHARACTERS)
        return "(%s) %s  " % (
            character, self.topgun_script.get_random(character)
        )

    def callback_message(self, conn, mess):
        """Listen for TOP GUN mentions and interject random lines from those
        characters who were mentioned.
        """
        if (mess.getFrom().getStripped() == config.BOT_IDENTITY["nickname"]) \
                or (get_sender_username(mess) == config.CHATROOM_FN):
            logging.debug("Ignore a message from myself")
            return False

        for character in self.topgun_script.CHARACTERS:
            search = "--" + character
            return search
            if mess.getBody().startswith(search):
                return "(%s) %s  " % (
                    character, self.topgun_script.get_random(character)
                )
