def transliterate(text):
    mapping = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH',
        'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Ъ': '', 'Ь': '', 'Э': 'E',
        'Ю': 'IU', 'Я': 'IA', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
        'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'ъ': '', 'ь': '',
        'э': 'e', 'ю': 'iu', 'я': 'ia'
    }

    result = ''
    for char in text:
        if char in mapping:
            tr_char = mapping[char]
            if char.isupper() and len(tr_char) > 1:
                tr_char = tr_char[0].upper() + tr_char[1:].lower()
            result += tr_char
        else:
            result += char
    return result

text_to_transliterate = input('Введите текст для транслитерации: ')
transliterated_text = transliterate(text_to_transliterate)
print('Транслитерированный текст:', transliterated_text)