# PagedJS HTML Sphinx Theme

## Background

This theme provides a [Sphinx](https://github.com/sphinx-doc/sphinx)
template that uses the [pagedjs](https://www.pagedjs.org/documentation/)
Javascript library to implement a few of the forthcoming
[CSS3 paged media](https://print-css.rocks/lessons) directives for pdf pagination and
headers/footers. It is  based on the pandoc template for
[rstudio/pagedown](https://github.com/rstudio/pagedown).

It was created by [Mara Colclough](https://github.com/maracieco) as part of the 
[EOAS/UBC courseware project](https://eoas-ubc.github.io/)

## Demonstration

An example build:

* [The original myst markdown](https://github.com/eoas-ubc/paged_html_theme/blob/master/examples/page_break_test/index.md)

* [The rendered html](https://phaustin.github.io/paged_html_theme/test_file.html)

## Installation

```
conda install -c eoas_ubc paged_html_theme

```

## Build the example

- clone the repository and cd to the directory

```
git clone https://github.com/eoas-ubc/paged_html_theme.git
cd paged_html_thme
``

- execute `build_page` to build the example
  if the `--generate_json` flag is given, a json file
  containing dummy header arguments and page margins is created.

```
build_page examples/page_break_test/test_file.md  \
  examples/page_break_test/headers.json --generate_json`
  ```
- this will write two files:

  `examples/page_break_test/_test_file_build/test_file.html`

and

  ``examples/page_break_test/headers.json`

- Edit `headers.json` to change headers.


## Development

```

- create the environment and activate

```
cd paged_html_theme
conda  env create --name theme_dev --file environment.yml
conda activate theme_dev
```

- compile the scss, insert the css into the jinja2 template and install

```
cd paged_html_theme
python inject_css.py
pip install -e .
```

- build the example as above

```
`build_page examples/page_break_test/test_file.md examples/page_break_test/headers.json --generate_json`
```

## Adjustable parameters/features

- To insert a pagebreak, use `<div class="page-break"></div>`

- To change the page size, or the left and center header edit headers.json

+++

## Next steps/notes

1. Make parameter setup compatible with the latex pdf builder via
   [issue 201](https://github.com/executablebooks/MyST-NB/issues/201)

2. Add bookmarks once chrome implements [781797](https://bugs.chromium.org/p/chromium/issues/detail?id=781797)
