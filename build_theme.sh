echo "Running Sass" 
sass --no-source-map .\src\scss\print_style.scss .\src\css\print_style.css
echo "Injecting CSS"
python.exe inject_css.py