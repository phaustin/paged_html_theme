# PagedJS HTML Sphinx Theme

## Installation and Building

1. Prepare your environment using the environment.yml file.

2. To install theme, run:

```
pip install -e .
```

3. To build the theme (inject stylesheet into HTML), run the following. This is a required step. If the CSS is linked to from the HTML, the page cannot load without the CSS file being hosted somewhere. This  works around that by putting the CSS inside <style> tags directly in the HTML. They are not combined from the beginning so that it is easier for developers.

```
python inject_css.py
```

4. Then you can build a sample by cd'ing into its folder and running:
```
sphinx-build -v -a -b html source _build/html
```

5. Now you should be able to open the index.html files located in each of the samples' \_build/html folders. 

## Notes
The current state of the sample quiz built from master can be found [here](https://hcolclou.github.io/paged_html_theme/).
