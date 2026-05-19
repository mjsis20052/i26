with open('proyectos_internos/agrirag_inta.html', 'r', encoding='utf-8') as f:
    content = f.read()

main_open = content.count('<main')
main_close = content.count('</main>')
div_open = content.count('<div')
div_close = content.count('</div>')

print(f"Main: {main_open} open, {main_close} close")
print(f"Div: {div_open} open, {div_close} close")
