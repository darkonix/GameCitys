import unittest
import main


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        main.check_list = []

    def test_normalize_city_name(self):
        text = "Гомёль Великий"
        self.assertEqual(main.normalize_city_name(text), "гомель великий")

    def test_check_point(self):
        main.check_point("poggers")
        self.assertEqual(["poggers"], main.check_list)

    def test_is_city_startswith_char(self):
        self.assertEqual(True, main.is_city_startswith_char("Киев", "К"))

    def test_is_non_cached(self):
        self.assertEqual(False, main.is_non_cached("Питер", ["Питер"]))

    def test_get_next_char(self):
        self.assertEqual("н", main.get_next_char("Ченый"))


if __name__ == '__main__':
    unittest.main()
