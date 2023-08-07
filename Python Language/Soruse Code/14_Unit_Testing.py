import unittest

def sum(a,b):
    return a+b


class test(unittest.TestCase):
    def testing_sum(self):
        result=sum(5,5)
        self.assertEqual(result,10)


if __name__ == "__main__":
    unittest.main()



