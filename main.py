lang_lbr = {
    '1': {
        '1': 'Выберите металл',
        '2': 'Введите количество грамм'
    },
    '2': {
        '1': 'Choose metal',
        '2': 'Enter how many metals'
    }
}


if __name__ == '__main__':
    lang = input('Выберите язык: | Chose your language: \n1 - RU | 2 - EN')
    metal = input(f'{lang_lbr[lang][1]}')
    neto = input(f'{lang_lbr[lang][2]}')


