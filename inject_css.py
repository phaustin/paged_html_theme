def inject_css(style, template, output):
    style_f = open(style, 'r')
    style_str = style_f.read()
    style_f.close()
    
    template_f = open(template, 'r')
    template_str = template_f.read()
    template_f.close()

    output_str = template_str.replace('/*INJECT_CSS_HERE*/', style_str, 1)

    output_f = open(output, 'w')
    output_f.write(output_str)
    output_f.close()

if __name__ == "__main__":
    inject_css('src/css/print_style.css', 'src/template.html', 'paged_html_theme/layout.html')