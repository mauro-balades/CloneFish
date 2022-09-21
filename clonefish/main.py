from art import text2art
from loguru import logger
from termcolor import colored, cprint

import sys

from clonefish.options import Options, OptionsManager

class Application:

    options: Options

    def __init__(self):
        """This contructor is used to get options
            and to get everything ready to start.
        """

        self.print_banner()

        self.set_options()
        self.initialize_logger()

    def initialize_logger(self) -> None:
        """Create new loggers with custom formats for
            the application to use.
        """

        info_prefix = colored("[+]", "blue", attrs=["bold"])
        debug_prefix = colored("[!]", "yellow", attrs=["bold"])
        error_prefix = colored("[~]", "red", attrs=["bold"])

        logger.add(sys.stdout, format=f"{info_prefix} {{message}}", level="INFO")
        logger.add(sys.stdout, format=f"{debug_prefix} {{message}}", level="DEBUG")
        logger.add(sys.stdout, format=f"{error_prefix} {{message}}", level="ERROR")


    def set_options(self) -> None:
        """This function is used to fetch
            the options given to the application.

            note that if there are no "required"
            parameters given to sys.argv, the `Application`
            will ask them by prompt.
        """

        argv = sys.argv

        # Check if any arguments has been
        # passed to `sys.argv`
        if len(argv) <= 1:
            # Get options by stdio prompts.
            self.options = OptionsManager.prompt()
        else:
            # TODO
            pass


    def print_banner(self) -> None:
        """This utility function is used to print some *sexy*
            ASCII art to the terminal.
        """

        lines = [
            text2art("CloneFish".center(20), font='tarty1', chr_ignore=True), # Return ASCII text with block font
            "",
            colored("[===]           CloneFish is only for educational pruposes!         [===]", "blue", attrs=["bold"]),
            colored("[===]           Created by Mauro Balades                            [===]", "blue", attrs=["bold"]),
            colored("[===]              (https://github.com/mauro-balades)               [===]", "blue", attrs=["bold"]),
            "",
            colored("                Welcome to CloneFish! Here, you can clone", "green", attrs=["bold"]),
            colored("                    websites and use them for fishing.", "green", attrs=["bold"]),
            ""
        ]

        for line in lines:
            print(line)
