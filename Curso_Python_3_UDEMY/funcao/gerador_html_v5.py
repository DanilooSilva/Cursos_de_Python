#! python3
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items()
                    if k in suportados)


def tab_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atrs)
    atributos = get_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class"{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {get_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    print(tab_bloco(tag_lista, 'Item1', 'Item2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))