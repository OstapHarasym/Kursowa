import unittest
import calc


# Клас з Unit - тестами для методу calc.integral
class TestIntegral(unittest.TestCase):
    # Тест на правильність результатів, які повертає метод calc.integral
    def test_integral(self):
        expected = 0.5
        actual = calc.integrate('x', '0', '1')[0]
        self.assertEqual(actual, expected)


# Клас з Unit - тестами для методу calc.differential
class TestDifferential(unittest.TestCase):
    # Тест на правильність результатів, які повертає метод calc.differential
    def test_differential(self):
        expected = True
        actual = calc.differential('y', '1', '0', '1')[0].success
        self.assertEqual(actual, expected)


# Клас з Unit - тестами для методу calc.progression_sum
class TestRow(unittest.TestCase):
    # Тест на правильність результатів, які повертає метод calc.progression_sum
    def test_sum(self):
        expected = 2564.0526520013423
        actual = calc.progression_sum('(sin(x) + exp(x))/5', 10)
        self.assertEqual(actual, expected)


# Клас з Unit - тестами для методу calc.lim
class TestLimit(unittest.TestCase):
    # Тест на правильність результатів, які повертає метод calc.lim
    def test_limit(self):
        expected = 0
        actual = calc.lim('1/x', 'oo')
        self.assertEqual(actual, expected)


# Клас з Unit - тестами для методу calc.determinant
class TestMatrix(unittest.TestCase):
    # Тест на правильність результатів, які повертає метод calc.determinant
    def test_determinant(self):
        test_data = ['0', '1', '2', '3', '4', '5', '6', '7', '1', 'Порахувати визначник']
        expected = 21.0
        actual = calc.determinant(test_data)
        self.assertEqual(actual, expected)


# Запуск всіх Unit - тестів
if __name__ == '__main__':
    unittest.main()
