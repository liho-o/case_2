lang_lbr = {
    '1': {
        '1': 'Выберите металл',
        '2': 'Введите количество грамм'
    }
}
def choes(lang):
    first_mes = ''
    metal = input(f'{lang_lbr[lang][1]}')


if __name__ == '__main__':
    lang = input('Выберите язык: | Chose your language: \n1 - RU | 2 - EN')
    choes(lang)

