import unittest
from lib import count_common_elements

class TestCountCommonElements(unittest.TestCase):

    def test_no_common_elements(self):
        # Тест, если в списках нет одинаковых элементов
        result = count_common_elements([1, 2, 3], [4, 5, 6], [7, 8, 9])
        self.assertEqual(result, 0)

    def test_some_common_elements(self):
        # Тест с несколькими общими элементами
        result = count_common_elements([1, 2, 3], [3, 4, 5], [5, 6, 7])
        self.assertEqual(result, 2)  # Общие элементы: 3 и 5

    def test_all_common_elements(self):
        # Тест, если все элементы общие
        result = count_common_elements([1, 2], [1, 2], [1, 2])
        self.assertEqual(result, 2)

    def test_empty_lists(self):
        # Тест с пустыми списками
        result = count_common_elements([], [], [])
        self.assertEqual(result, 0)

    def test_single_list(self):
        # Тест с одним списком (нет других списков для сравнения)
        result = count_common_elements([1, 2, 3])
        self.assertEqual(result, 0)

    def test_duplicates_in_lists(self):
        # Тест со списками, содержащими повторяющиеся элементы
        result = count_common_elements([1, 1, 2, 2], [2, 3, 3], [1, 3, 4])
        self.assertEqual(result, 3)  # Общие элементы: 1, 2, 3

if __name__ == '__main__':
    unittest.main()