from collections import Counter

def count_common_elements(*lists):
    # Объединяем все списки в один
    all_elements = [element for sublist in lists for element in sublist]

    # Подсчитываем количество вхождений каждого элемента
    element_counts = Counter(all_elements)

    # Считаем количество элементов, встречающихся хотя бы в двух списках
    common_count = sum(1 for count in element_counts.values() if count > 1)

    return common_count


def main():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    list3 = [4, 6, 7, 8]

    common_elements_count = count_common_elements(list1, list2, list3)
    print("Количество одинаковых элементов:", common_elements_count)

if __name__ == '__main__':
    main()
