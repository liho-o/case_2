# Part of case-study #2: Alloys
# Developer: Solodovnik A., Kim A., Kabanova M., Soknyshev D.
#

import lang_templates
import ferum
import cuprum
import nickel

lang_lbr = lang_templates.lang_lbr  # Rename file


def previous():  # Requesting user input
    """
    First function.
    :return: lang, metal, neto
    """

    lang = str(input('Выберите язык: | Chose your language: \n1 - RU | 2 - EN\n'))
    metal = input(f'{lang_lbr[lang]["1"]}')
    neto = int(input(f'{lang_lbr[lang]["2"]}'))
    return lang, metal, neto


def main(lang, metal, neto):
    """
    Main function.
    :return: None
    """

    if metal == 'fe':
        main_dict = ferum

    elif metal == 'cu':
        main_dict = cuprum

    elif metal == 'ni':
        main_dict = nickel

    else:
        print(f'{lang_lbr[lang]["0"]}')
        return

    for alloy in main_dict.alloys[lang]:
        local_alloy = main_dict.alloys[lang][alloy]  # Alloys for this metal
        local_alloy_neto = local_alloy[metal]  # Adresses percentage of metal for alloy
        total_alloy_neto = round(neto / local_alloy_neto, 2)  # Counting final alloy mass

        print(f'{lang_lbr[lang]["3"]} {alloy} {total_alloy_neto} {lang_lbr[lang]["4"]}')
        print(f'{lang_lbr[lang]["5"]}')

        for material in main_dict.alloys[lang][alloy]:  # Cycle for missing elements
            if metal == material:
                continue
            metal_koef = main_dict.alloys[lang][alloy][material]  # Adresses percentage of missing for alloy
            request = round(total_alloy_neto * metal_koef, 2)  # Counting missing elements
            print(material, ' --- ', request, end='\n')


if __name__ == '__main__':  # Run only if this file is active
    lang, metal, neto = previous()
    main(lang, metal, neto)
