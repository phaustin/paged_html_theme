import click
from pathlib import Path
import context
import sass

def compile_scss(in_scss, out_css):
    """
    compile in_scss to out_css

    """
    css_dir = Path(out_css).parent
    css_dir.mkdir(parents=True, exist_ok = True)
    css_string = sass.compile(filename=in_scss)
    with open(out_css, 'w', encoding = "utf8") as outfile:
        outfile.write(css_string)

def inject_css(style_file, template_j2, layout_html):
    """
    inject the css styles of style_file into template_j2

    Parameters
    ----------

    style_file: str
        path to print_style.css

    template_j2: str
        path to jinja2 template

    layout_html: str
        path to jinja2 template with injected css

    Returns
    -------

    None
    """

    with open(style_file, 'r', encoding = "utf8") as style_f:
        style_str = style_f.read()
        
    with open(template_j2, 'r', encoding = "utf8") as template_f:
        template_str = template_f.read()

    output_str = template_str.replace('/*INJECT_CSS_HERE*/', style_str, 1)

    with open(layout_html,'w', encoding="utf8") as output_f:
        output_f.write(output_str)


if __name__ == "__main__":
    in_scss = str(context.root_dir / 'src/scss/print_style.scss')
    out_css = str(context.root_dir / 'src/css/print_style.css')
    compile_scss(in_scss, out_css)
    template_j2 = str(context.root_dir / 'src/template.html')
    layout_j2 = str(context.root_dir / 'paged_html_theme/layout.html')
    inject_css(out_css, template_j2, layout_j2)
