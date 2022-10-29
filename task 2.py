x = {} # создание словаря
def get_count_char(str_):
    s = []  # TODO посчитать количество каждой буквы в строке в аргументе str_

    for i in str_.lower():
        if i.isalpha():
            s.append(i)

    for i in s:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    return x

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
def convert(x):
    new = {}
    c = 0
    d = 0
    e = 0
    for v,z, in x.items():
        new[v] = round(z/sum(x.values())),
    c = 1-sum(new.values())
    for k,i in new.items():
        if i > e:
            e = i
            d = k
    new[d] = e + c
    return new
print(convert(x))