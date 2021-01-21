def tag_bloco(texto, clase='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{clase}">{texto}</{tag}>'


if __name__ == '__main__':
    # Testes (assertions)
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
