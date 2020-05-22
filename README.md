# PagedJS HTML Sphinx Theme

1. To prepare environment, follow instructions at [paged_trio](https://github.com/eoas-ubc/paged_trio/blob/master/Readme.md)

2. To install theme, run:

```
pip install -e .
```

3. To build the theme (inject stylesheet into HTML), run the following. This is a required step. If the CSS is linked to from the HTML, the page cannot load without the CSS file being hosted somewhere. This  works around that by putting the CSS inside <style> tags directly in the HTML. They are not combined from the beginning so that it is easier for developers.

```
build_theme.ps1
```

4. To build the samples, run:
```
build_all.ps1
```

5. Now you should be able to open the index.html files located in each of the samples' build folders.

