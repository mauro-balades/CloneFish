from multiprocessing.context import set_spawning_popen
import sys

from clonefish.options import Options, OptionsManager

class Application:

    options: Options
    def __init__(self):
        """This contructor is used to get options
            and to get everything ready to start.
        """

        self.set_options()

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

