
def pars(strok):
    str1 = ''
    slovar = {
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'ж':'g',
    'е':'e',
    'ё':'e',
    'з':'z',
    'и':'i',
    'й':'y',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'c',
    'ч':'ch',
    'ш':'sh',
    'щ':'sh',
    'ы':'i',
    'э':'e',
    'ю':'yu',
    'я':'ya',
    ' ':'_',
    'ъ':'',
    'Ъ':'',
    'ь':'',
    'Ь':'',
    'А':'a',
    'Б':'b',
    'В':'v',
    'Г':'g',
    'Д':'d',
    'Ж':'g',
    'Е':'e',
    'Ё':'e',
    'З':'z',
    'И':'i',
    'Й':'y',
    'К':'k',
    'Л':'l',
    'М':'m',
    'Н':'n',
    'О':'o',
    'П':'p',
    'Р':'r',
    'С':'s',
    'Т':'t',
    'У':'u',
    'Ф':'f',
    'Х':'h',
    'Ц':'c',
    'Ч':'ch',
    'Ш':'sh',
    'Щ':'sh',
    'Ы':'i',
    'Э':'e',
    'Ю':'yu',
    'Я':'ya',
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9',
    '0':'0',
    }
    for i in strok:
        if i in slovar.keys():
            str1 += slovar[i]
        else:
            str1+=''
    return str1
