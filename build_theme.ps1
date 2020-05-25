Write-Output "Running Sass" 
sass --no-source-map .\src\scss\print_style.scss .\src\css\print_style.css
Write-Output "Injecting CSS"
python.exe inject_css.py