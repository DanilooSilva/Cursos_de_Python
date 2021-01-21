def tag_bloco(texto, clase='success'):
    return f'<div class="{clase}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'
    print(tag_bloco('bloco'))

