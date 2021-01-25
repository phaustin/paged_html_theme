import importlib_resources as ir
import click
import jinja2
from pathlib import Path
import subprocess
import contextlib
import os
import json
import pprint


@contextlib.contextmanager
def cd(path):
    #print(f'initially inside {os.getcwd()}')
    CWD = os.getcwd()
    os.chdir(path)
    #print(f'inside {os.getcwd()}')
    try:
        yield
    except Exception as e:
        print(f'Exception caught: {e}')
    finally:
        #print(f'returning to {os.getcwd()}')
        os.chdir(CWD)


header_dict=dict(page_title = 'Day 03 quiz',
              left_header = 'Jan. 19, 2021',
              center_header = 'Day 03 quiz')


@click.command()
@click.argument('myst_file',type=str)
@click.argument('header_file',type=str)
@click.option('--generate_json',is_flag=True, help='generate sample headers.json')
def main(myst_file,header_file,generate_json):
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
    myst_file = Path(myst_file).resolve()
    header_file = Path(header_file).resolve()
    stem_name = myst_file.stem
    root_dir = myst_file.parent
    output_dir = root_dir /  f'_{stem_name}_build'
    if generate_json:
        with ir.open_text('paged_html_theme.templates','headers.json',encoding='utf-8') as header_in:
            header_contents = header_in.read()
        with open(header_file,'w',encoding='utf-8') as header_out:
            header_out.write(header_contents)
        print(f"wrote sample header file \n{header_contents} to \n{str(header_file)}\n")
    with open(header_file,'r',encoding='utf-8') as input:
        header_dict = json.load(input)
    contents=list(ir.contents('paged_html_theme.templates'))
    with ir.open_text('paged_html_theme.templates','conf_py.j2',encoding='utf-8') as the_conf:
        conf_j2 = jinja2.Template(the_conf.read())
    if not Path(myst_file).is_file():
        raise ValueError(f"could not find {myst_file}")
    arglist = ['sphinx-build','-v', '-b html',str(root_dir),str(output_dir), str(myst_file)]
    argstring = ' '.join(arglist)
    header_dict['stem_name']=stem_name
    conf_file = conf_j2.render(**header_dict)
    with cd(root_dir):
        with open('conf.py','w',encoding='utf-8') as conf_out:
            conf_out.write(conf_file)
        print(f"running the command \n{argstring}\n")
        result = subprocess.run(argstring, capture_output=True, shell=True)
    if result.stdout:
         print(f"stdout message: {result.stdout.decode('utf-8')}")
         out_file = output_dir / f"{stem_name}.html"
         if out_file.is_file():
             print(f"full path to output: {out_file}")
         else:
             raise ValueError(f"can't find output file {out_file}")
    if result.stderr:
        print(f"stderror message: {result.stderr.decode('utf-8')}")


