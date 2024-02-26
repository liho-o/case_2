import lang_templates

lang_lbr = lang_templates.lang_lbr


def previos():
    lang = input('Выберите язык: | Chose your language: \n1 - RU | 2 - EN')
    metal = input(f'{lang_lbr[lang][1]}')
    neto = input(f'{lang_lbr[lang][2]}')
    return lang, metal, neto


def main(lang, metal, neto):
    pass


if __name__ == '__main__':
    lang, metal, neto = previos()
    main(lang, metal, neto)




