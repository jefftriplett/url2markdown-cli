===============================
url2markdown-cli
===============================

Fetch a url and translate it to markdown in one command.


Usage
-----

First, get cookiecutter. Trust me, it's awesome::

.. code-block:: bash

    $ pip install url2markdown-cli

To use:

.. code-block:: bash

    python url2markdown-cli.py --with-cache https://www.djangoproject.com/

To use your own custom url2markdown server instance (you should):

.. code-block:: bash

    export URL2MARKDOWN_URL='http://url2markdown.herokuapp.com/?url={url}'


Thanks
------

Thanks to @kennethreitz for his url2markdown project which this compliments:
    (https://github.com/kennethreitz/url2markdown)
