import unittest
from decimal import Decimal
from converter import Converter
from manager import CurrencyCode
from reader import load_to_db

class TestConverter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_to_db()
        cls.converter = Converter()

    def test_convert_usd_to_eur(self):
        amount = Decimal("100")
        date = "2025-09-16"
        result = self.converter.convert(amount, CurrencyCode.USD, CurrencyCode.EUR, date)
        self.assertIsInstance(result, Decimal)
        self.assertGreater(result, Decimal("0"))

    def test_same_currency(self):
        amount = Decimal("50")
        date = "2025-09-16"
        result = self.converter.convert(amount, CurrencyCode.USD, CurrencyCode.USD, date)
        self.assertEqual(result, amount)

if __name__ == "__main__":
    unittest.main()