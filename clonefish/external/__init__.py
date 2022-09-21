
from clonefish.options import Options
from clonefish.utils import is_valid_url, throw_error
from loguru import logger

import requests

# TODO: inherit from a parent class called "Provider"
class ExternalProvider:
    options: Options
    def __init__(self, options: Options) -> None:
        self.options = options

    def execute(self):
        url = self.options.external_opts['url']
        if not is_valid_url(url):
            throw_error(f"'{url}' is not a valid URL!")

        logger.info(f"Fetching website contents from '{url }'")

        try:
            response = requests.get(url)
        except Exception as e:
            throw_error(f"found an error while fetching website: {e}")

