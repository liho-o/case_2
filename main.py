import lang_templates
import ferum

lang_lbr = lang_templates.lang_lbr


def previos():
    lang = str(input('Выберите язык: | Chose your language: \n1 - RU | 2 - EN\n'))
    metal = input(f'{lang_lbr[lang]["1"]}')
    neto = int(input(f'{lang_lbr[lang]["2"]}'))
    return lang, metal, neto


def main(lang, metal, neto):
    for alloy in ferum.alloys[lang]:
        local_alloy = ferum.alloys[lang][alloy]
        local_alloy_neto = local_alloy[metal]
        # print(neto, local_alloy_neto)
        total_alloy_neto = neto / local_alloy_neto
        print(f'{lang_lbr[lang]["3"]}', alloy, total_alloy_neto, f'{lang_lbr[lang]["4"]}')
        print(f'{lang_lbr[lang]["5"]}')
        for matireal in ferum.alloys[lang][alloy]:
            if metal == matireal:
                continue
            metal_koef = ferum.alloys[lang][alloy][matireal]
            request = total_alloy_neto * metal_koef
            print(matireal, ' --- ', request)

        print(' ')


if __name__ == '__main__':
    lang, metal, neto = previos()
    main(lang, metal, neto)
