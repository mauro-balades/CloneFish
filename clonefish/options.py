
from enum import Enum
import questionary

class Options:
    class CommandType(Enum):
        EXTERNAL = 0
        TEMPLATE = 1

    id: CommandType
    external_opts = { "url": "" }


class OptionsManager:

    command_types = {
        "Copy from external website": Options.CommandType.EXTERNAL,
        "Use predefined template": Options.CommandType.TEMPLATE
    }

    def prompt(self) -> Options:
        """Get the options by asking prompting
        to stdio.

        Returns:
            Options: Options retrieved from prompt
        """

        options = Options()

        command_type = str(questionary.select(
            "What do you want to do?",
            choices=self.command_types,
        ).ask())

        options.id = self.command_types[command_type]
        if options.id == Options.CommandType.EXTERNAL:
            url = questionary.text("Please type the login pacge for the URL:").ask()
            options.external_opts["url"] = str(url)

        return options
