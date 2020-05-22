from setuptools import setup

setup(
    name='paged-html-theme',
    version="0.1",
    entry_points = {
        'sphinx.html_themes': [
            'paged_html_theme = paged_html_theme',
        ]
    },
)
