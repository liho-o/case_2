# Part of case-study #2: Alloys
# Developer: Solodovnik A., Kabanova M., Soknyshev D., Kim A.
#

import lang_templates
import ferum

lang_lbr = lang_templates.lang_lbr


def previos():
    lang = input('Выберите язык: | Chose your language: \n1 - RU | 2 - EN\n')
    metal = input(f'{lang_lbr[lang][1]}')
    neto = input(f'{lang_lbr[lang][2]}')
    return lang, metal, neto


def main(lang, metal, neto):
    # metal = 'fe'
    # neto = 100
    for alloy in ferum.alloys:
        print(alloy)
        local_alloy = ferum.alloys[alloy]
        local_alloy_neto = local_alloy[metal]
        total_alloy_neto = neto / local_alloy_neto
        for material in ferum.alloys[alloy]:
            if metal == material:
                continue
            metal_koef = ferum.alloys[alloy][material]
            request = total_alloy_neto * metal_koef
            print(material, ' --- ', request)

        print(total_alloy_neto, end='\n\n')


if __name__ == '__main__':
    lang, metal, neto = previos()
    main(lang, metal, neto)
