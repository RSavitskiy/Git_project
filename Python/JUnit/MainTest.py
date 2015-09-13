# coding=utf-8
import unittest
# import func
# from module import func
import MethodForTest


class MainTest(unittest.TestCase):
    # test is the sum of two values
    def test_sum(self):
        self.assertEqual(MethodForTest.summ(15, 15), 30)

    # test is the multiplication of two values
    def test_multi(self):
        self.assertEqual(MethodForTest.multi(15, 2), 30)

    #test is the string
    def test_string(self):
        self.assertEqual(MethodForTest.string("xx", 3), "xxxxxx")

    #find items in the list
    def test_list(self):
        self.assertEqual(MethodForTest.list(5), 5)

    #test values ​​are not equal
    def test_notEqual(self):
        self.assertNotEquals(MethodForTest.notEquil(5, 5), 24)

    #test equal dictionary
    def test_dist(self):
        self.assertDictEqual({"Nif": 1, "Nyf": 2, "Naf": 3}, {"Nif": 1, "Nyf": 2, "Naf": 3})


# if __name__ == '__main__':
# unittest.main()


suite = unittest.TestLoader().loadTestsFromTestCase(MainTest)
unittest.TextTestRunner(verbosity=2).run(suite)


