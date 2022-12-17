from unittest import TestCase, main
from Sp import read_saves
from Sp import write_saves
from Sp import key

class SpTests(TestCase):
    def test_read_saves(self):
        self.l = [ ]
        self.assertEqual(read_saves(self.l, "TestSaves.txt"), ["1", "2", "3", "4", "5", "6", "7", "8", '9'])
    def test_write_saves(self):
        self.l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        write_saves(self.l, "TestSaves.txt" )
        self.assertEqual(read_saves(self.l, "TestSaves.txt"), ["1", "2", "3", "4", "5", "6", "7", "8", '9'])
    def test_on_press_True(self):
        self.k = key(1, 0, 1)
        self.assertEqual(self.k.on_press(), True)
    def test_on_release_True(self):
        self.k = key(1, 1, 0)
        self.assertEqual(self.k.on_release(), True)
    def test_on_press_False(self):
        self.k = key(1, 1, 0)
        self.assertEqual(self.k.on_press(), False)
    def test_on_release_False(self):
        self.k = key(1, 0, 1)
        self.assertEqual(self.k.on_release(), False)


if __name__ == "__main__":
    main()