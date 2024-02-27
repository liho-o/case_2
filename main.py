import lang_templates
import ferum
import cuprum
import nickel

lang_lbr = lang_templates.lang_lbr  # Rename file


def previous():  # Requesting user input
    lang = str(input('Выберите язык: | Chose your language: \n1 - RU | 2 - EN\n'))
    metal = input(f'{lang_lbr[lang]["1"]}')
    neto = int(input(f'{lang_lbr[lang]["2"]}'))
    return lang, metal, neto


def main_calculations(lang, metal, neto, main_dict):
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


def main(lang, metal, neto):
    if metal == 'fe':
        main_dict = ferum

    if metal == 'cu':
        main_dict = cuprum

    if metal == 'ni':
        main_dict = nickel

    else:
        print(f'{lang_lbr[lang]["0"]}')
        return
    main_calculations(lang, metal, neto, main_dict)



if __name__ == '__main__':  # Run only if this file is active
    lang, metal, neto = previous()
    main(lang, metal, neto)
