from os import path

def setup(app):
    app.add_stylesheet('_static/static_theme_files/css/custom.css')
    app.add_html_theme('paged_html_theme', path.abspath(path.dirname(__file__)))