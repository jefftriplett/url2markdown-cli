# url2markdown-cli

Fetch a url and translate it to markdown in one command.

## Usage

To install:

```shell
$ pip install url2markdown-cli
```

To use:

```shell
url2markdown --with-cache https://www.djangoproject.com/
```

To use your own custom url2markdown server instance (you should):

```shell
export URL2MARKDOWN_URL='http://markdownplease.com/?url={url}'
```

## Thanks

Thanks to @kennethreitz for his [url2markdown](https://github.com/kennethreitz/url2markdown) project which this compliments.
