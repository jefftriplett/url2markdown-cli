# -*- coding: utf-8 -*-
"""

Thanks to @kennethreitz for his url2markdown project which this compliments:
    (https://github.com/kennethreitz/url2markdown)

To install library dependencies:
    pip install click requests requests-cache

To use:
    python url2markdown-cli.py --with-cache https://www.djangoproject.com/

To use your own custom url2markdown server instance:
    export URL2MARKDOWN_URL='http://url2markdown.herokuapp.com/?url={url}'

"""

import click
import os
import requests

try:
    import requests_cache
except ImportError:
    requests_cache = None

__author__ = 'Jeff Triplett'
__email__ = 'jeff.triplett@gmail.com'
__version__ = '0.4.1'

URL2MARKDOWN_URL = os.environ.get('URL2MARKDOWN_URL', 'http://markdownplease.com/?url={url}')


def url2markdown(url):
    req = requests.get(URL2MARKDOWN_URL.format(url=url))
    return req.text


@click.command()
@click.argument('url')
@click.option('--with-cache', is_flag=True)
def main(url, with_cache):
    if with_cache:
        if requests_cache is None:
            raise NotImplementedError(
                'The --with-cache option requires that `requests-cache` to be installed. '
                'Try `pip install url2markdown-cli[requests-cache]`.'
            )

        requests_cache.install_cache()

    click.echo(url2markdown(url))


if __name__ == '__main__':
    main()
