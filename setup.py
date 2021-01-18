from setuptools import setup

setup(
    name='paged-html-theme',
    version="0.2",
    packages=["paged_html_theme"],
    include_package_data=True,
    entry_points = {
        'sphinx.html_themes': [
            'paged_html_theme = paged_html_theme'
        ],
        'console_scripts' : [
            'build_page = paged_html_theme.scripts.build_page:main'
        ]
    },
    install_requires=[
        'sphinx>=3.1',
        'importlib_resources']
)
