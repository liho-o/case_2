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


def main(lang, metal, neto):
    if metal == 'fe':
        for alloy in ferum.alloys[lang]:
            local_alloy = ferum.alloys[lang][alloy]  # Alloys for this metal
            local_alloy_neto = local_alloy[metal]  # Adresses percentage of metal for alloy
            total_alloy_neto = round(neto / local_alloy_neto, 2)  # Counting final alloy mass

            print(f'{lang_lbr[lang]["3"]} {alloy} {total_alloy_neto} {lang_lbr[lang]["4"]}')
            print(f'{lang_lbr[lang]["5"]}')

            for material in ferum.alloys[lang][alloy]:  # Cycle for missing elements
                if metal == material:
                    continue
                metal_koef = ferum.alloys[lang][alloy][material]  # Adresses percentage of missing for alloy
                request = round(total_alloy_neto * metal_koef, 2)  # Counting missing elements
                print(material, ' --- ', request)
            print('')

    if metal == 'cu':
        for alloy in cuprum.alloys[lang]:
            local_alloy = cuprum.alloys[lang][alloy]  # Alloys for this metal
            local_alloy_neto = local_alloy[metal]  # Adresses percentage of metal for alloy
            total_alloy_neto = round(neto / local_alloy_neto, 2)  # Counting final alloy mass

            print(f'{lang_lbr[lang]["3"]} {alloy} {total_alloy_neto} {lang_lbr[lang]["4"]}')
            print(f'{lang_lbr[lang]["5"]}')

            for material in cuprum.alloys[lang][alloy]:  # Cycle for missing elements
                if metal == material:
                    continue
                metal_koef = cuprum.alloys[lang][alloy][material]  # Adresses percentage of missing for alloy
                request = round(total_alloy_neto * metal_koef, 2)  # Counting missing elements
                print(material, ' --- ', request)
            print('')

    if metal == 'ni':
        for alloy in nickel.alloys[lang]:
            local_alloy = nickel.alloys[lang][alloy]  # Alloys for this metal
            local_alloy_neto = local_alloy[metal]  # Adresses percentage of metal for alloy
            total_alloy_neto = round(neto / local_alloy_neto, 2)  # Counting final alloy mass

            print(f'{lang_lbr[lang]["3"]} {alloy} {total_alloy_neto} {lang_lbr[lang]["4"]}')
            print(f'{lang_lbr[lang]["5"]}')

            for material in nickel.alloys[lang][alloy]:  # Cycle for missing elements
                if metal == material:
                    continue
                metal_koef = nickel.alloys[lang][alloy][material]  # Adresses percentage of missing for alloy
                request = round(total_alloy_neto * metal_koef, 2)  # Counting missing elements
                print(material, ' --- ', request)
            print('')


if __name__ == '__main__':  # Run only if this file is active
    lang, metal, neto = previous()
    main(lang, metal, neto)
