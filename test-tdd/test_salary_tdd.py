import unittest


def get_tax(income):
    if income <= 0:
        tax = 0

    elif income <= 150001:
        tax = (income - 150000) * 0.05

    elif income <= 300001:
        tax = (income-300000) * 0.10 + 7500

    elif income <= 500001:
        tax = (income-500000) * 0.15 + 37500

    return tax




class TestCase(unittest.TestCase):

    def test_salary_0(self):
        self.assertEqual(get_tax(0.00), 0)

    def test_salary_150000(self):
        self.assertEqual(get_tax(150000.00), 0)

    def test_salart_150001(self):
        self.assertEqual(get_tax(150001.00), 0.05)

    def test_salart_300000(self):
        self.assertEqual(get_tax(300000.00), 7500.0)

    def test_salart_300001(self):
        self.assertEqual(get_tax(300001.00),7500.1)

    def test_salart_500001(self):
        self.assertEqual(get_tax(500001.00),37500.15)


if __name__ == '__main__':
    unittest.main()
