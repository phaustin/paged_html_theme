from setuptools import setup

setup(
    name='paged-html-theme',
    version="0.1",
    packages=["paged_html_theme"],
    include_package_data=True,
    entry_points = {
        'sphinx.html_themes': [
            'paged_html_theme = paged_html_theme'
        ]
    },
    install_requires=['sphinx<3']
)
