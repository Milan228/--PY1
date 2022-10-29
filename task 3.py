def delete(list_, index=None):
    if index == None:
        c = 0
    else:
        c = index
    a = list(set(list_[:c]))
    b = list(set(list_[c:]))
    return a + b
    ...  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
