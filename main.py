import lang_templates
import ferum
import cuprum
import nickel

lang_lbr = lang_templates.lang_lbr


def previos():
    lang = str(input('Выберите язык: | Chose your language: \n1 - RU | 2 - EN\n'))
    metal = input(f'{lang_lbr[lang]["1"]}')
    neto = int(input(f'{lang_lbr[lang]["2"]}'))
    return lang, metal, neto


def main(lang, metal, neto):
    if metal == 'fe':
        for alloy in ferum.alloys[lang]:
            local_alloy = ferum.alloys[lang][alloy]
            local_alloy_neto = local_alloy[metal]
            total_alloy_neto = round(neto / local_alloy_neto, 2)

            print(f'{lang_lbr[lang]["3"]}', alloy, total_alloy_neto, f'{lang_lbr[lang]["4"]}')
            print(f'{lang_lbr[lang]["5"]}')

            for material in ferum.alloys[lang][alloy]:
                if metal == material:
                    continue
                metal_koef = ferum.alloys[lang][alloy][material]
                request = round(total_alloy_neto * metal_koef, 2)
                print(material, ' --- ', request)
            print('')
    if metal == 'cu':
        for alloy in cuprum.alloys[lang]:
            local_alloy = cuprum.alloys[lang][alloy]
            local_alloy_neto = local_alloy[metal]
            total_alloy_neto = round(neto / local_alloy_neto, 2)

            print(f'{lang_lbr[lang]["3"]}', alloy, total_alloy_neto, f'{lang_lbr[lang]["4"]}')
            print(f'{lang_lbr[lang]["5"]}')

            for material in cuprum.alloys[lang][alloy]:
                if metal == material:
                    continue
                metal_koef = cuprum.alloys[lang][alloy][material]
                request = round(total_alloy_neto * metal_koef, 2)
                print(material, ' --- ', request)
            print('')
    if metal == 'ni':
        for alloy in nickel.alloys[lang]:
            local_alloy = nickel.alloys[lang][alloy]
            local_alloy_neto = local_alloy[metal]
            total_alloy_neto = round(neto / local_alloy_neto, 2)

            print(f'{lang_lbr[lang]["3"]}', alloy, total_alloy_neto, f'{lang_lbr[lang]["4"]}')
            print(f'{lang_lbr[lang]["5"]}')

            for material in nickel.alloys[lang][alloy]:
                if metal == material:
                    continue
                metal_koef = nickel.alloys[lang][alloy][material]
                request = round(total_alloy_neto * metal_koef, 2)
                print(material, ' --- ', request)
            print('')


if __name__ == '__main__':
    lang, metal, neto = previos()
    main(lang, metal, neto)
