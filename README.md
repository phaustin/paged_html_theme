# PagedJS HTML Sphinx Theme

## Background

This theme provides a [Sphinx](https://github.com/sphinx-doc/sphinx)
template that uses the [pagedjs](https://www.pagedjs.org/documentation/)
Javascript library to implement a few of the forthcoming
[CSS3 paged media](https://print-css.rocks/lessons) directives for pdf pagination and
headers/footers. It is  based on the pandoc template for
[rstudio/pagedown](https://github.com/rstudio/pagedown).

It was created by [Harlan Colclough](https://github.com/hcolclou) as part of the 
[EOAS/UBC courseware project](https://eoas-ubc.github.io/)

## Demonstration

An example build:

* [The original myst markdown](https://github.com/eoas-ubc/paged_html_theme/blob/master/examples/page_break_test/index.md)

* [The rendered html](https://phaustin.github.io/paged_html_theme/)

## Installation

1. conda

   ```conda install -c eoas_ubc paged_html_theme```

2. development

- clone the repository

```
git clone https://github.com/eoas-ubc/paged_html_theme.git
```

- create the environment and activate

```
cd paged_html_theme
conda env create -f environment.yml
conda activate buildit
```

- compile the scss, insert into the template and install

```
cd paged_html_theme
python inject_css.py
pip install -e .
```

- build the example

```
cd examples
sphinx-build -v -a -b html page_break_test  page_break_test/_build/html
```

- the processed html is `page_break_test/_build/html/index.html`

## Adjustable parameters/features

- To insert a pagebreak, use `<div class="page-break"></div>`

- To change the page size, or the left and center header edit the
[html_context](https://github.com/eoas-ubc/paged_html_theme/blob/16bded6351d782f7f279f8d169dcf73e603c274d/examples/page_break_test/conf.py#L58-L65)

  
## Next steps/notes

1. Make parameter setup compatible with the latex pdf builder

2. Add bookmarks once chrome implements [781797](https://bugs.chromium.org/p/chromium/issues/detail?id=781797)

