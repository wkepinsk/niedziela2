import unittest

class PierwszyTest(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu")
    def test_224(self):
        #'prawdziwy test'
        assert(2+2==4)
    def tearDown(self):
        print("sprzatem po testach")

if __name__ =='__main__':
    unittest.main(verbosity=2)