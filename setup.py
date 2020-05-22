from setuptools import setup

setup(
    name='paged-html-theme',
    version="0.1",
    packages=["paged_html_theme"],
    entry_points = {
        'sphinx.html_themes': [
            'paged_html_theme = paged_html_theme',
        ]
    },
)
