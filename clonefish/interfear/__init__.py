
from clonefish.options import Options

# TODO: inherit from a parent class called "Provider"
class InterfereProvider:
    options: Options

    def __init__(self, options: Options) -> None:
        self.options = options

    def execute(self):
        pass
