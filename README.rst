===============================
url2markdown-cli
===============================

Fetch a url and translate it to markdown in one command.


Usage
-----

To install:

.. code-block:: bash

    $ pip install url2markdown-cli

To use:

.. code-block:: bash

    url2markdown --with-cache https://www.djangoproject.com/

To use your own custom url2markdown server instance (you should):

.. code-block:: bash

    export URL2MARKDOWN_URL='http://markdownplease.com/?url={url}'


Thanks
------

Thanks to @kennethreitz for his url2markdown project which this compliments:
    (https://github.com/kennethreitz/url2markdown)
