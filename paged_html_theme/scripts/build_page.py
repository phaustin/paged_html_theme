import importlib_resources as ir
import click
import jinja2
from pathlib import Path
import subprocess
import contextlib
import os
import json

@contextlib.contextmanager
def cd(path):
    print(f'initially inside {os.getcwd()}')
    CWD = os.getcwd()
    os.chdir(path)
    print(f'inside {os.getcwd()}')
    try:
        yield
    except Exception as e:
        print(f'Exception caught: {e}')
    finally:
        print(f'returning to {os.getcwd()}')
        os.chdir(CWD)


header_dict=dict(page_title = 'Day 03 quiz',
              left_header = 'Jan. 19, 2021',
              center_header = 'Day 03 quiz')


@click.command()
@click.argument('myst_file',type=str)
@click.argument('header_file',type=str)
def main(myst_file,header_file):
    """
    Build a web page for the markdown file myst_file, using the headers in
    header_file, where header_file is a json file with a dictionary with
    these keys (margin sizes in inches)
    
    \b
    {
        "page_title": "Day 03 quiz",
        "left_header": "Jan. 19, 2021",
        "center_header": "Day 03 quiz",
        "page_margin_top": 1,
        "page_margin_bottom": 1,
        "page_margin_left": 1,
        "page_margin_right": 1
    }

    usage: build_page quiz3.md headers.json

    """
    with open(header_file,'r') as input:
        header_dict = json.load(input)
    contents=list(ir.contents('paged_html_theme.templates'))
    with ir.open_text('paged_html_theme.templates','conf_py.j2') as the_conf:
        conf_j2 = jinja2.Template(the_conf.read())
        myst_file = Path(myst_file).resolve()
    if not Path(myst_file).is_file():
        raise ValueError(f"could not find {myst_file}")
    stem_name = myst_file.stem
    header_dict['stem_name']=stem_name
    conf_file = conf_j2.render(**header_dict)
    root_dir = myst_file.parent
    output_dir = root_dir /  f'{stem_name}_build'
    root_dir = root_dir
    arglist = ['sphinx-build','-v', '-b html',str(root_dir),str(output_dir), str(myst_file)]
    argstring = ' '.join(arglist)
    with cd(root_dir):
        with open('conf.py','w') as conf_out:
            conf_out.write(conf_file)
        print(f"running the command \n{argstring}\n")
        result = subprocess.run(argstring, capture_output=True, shell=True)
    if result.stdout:
         print(f"stdout message: {result.stdout.decode('utf-8')}")
         out_file = output_dir / 'index.html'
         if out_file.is_file():
             print(f"full path to output: {out_file}")
         else:
             raise ValueError(f"can't fine output file {out_file}")
    if result.stderr:
        print(f"stderror message: {result.stderr.decode('utf-8')}")


