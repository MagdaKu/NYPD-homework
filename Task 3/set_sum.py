def set_sum(list1, list2):
    set_list = []
    for i in list1:
        if i not in set_list:
            set_list.append(i)
    for i in list2:
        if i not in set_list:
            set_list.append(i)
    return set_list
        

def sorted_set_sum(list1, list2):
    lista = set_sum(list1, list2)
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista


if __name__ == "__main__":
    print("Set sum:")
    print(set_sum([], []))
    print(set_sum([1, 2, 3], [1, 2, 3]))
    print(set_sum([], [1, 2, 3]))
    print(set_sum([1, 2, 3], []))
    print(set_sum([1, 3, -2], [-2, -3, 0, 1, 34]))
    print("Sorted set sum: ")
    print(sorted_set_sum([], []))
    print(sorted_set_sum([1, 2, 3], [1, 2, 3]))
    print(sorted_set_sum([], [1, 2, 3]))
    print(sorted_set_sum([1, 2, 3], []))
    print(sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]))
