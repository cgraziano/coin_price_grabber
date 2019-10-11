import unittest
from utils.key_extraction import getApiKeyFromFile

class TestKeyExtraction(unittest.TestCase):

    def testExtraction(self):
        filePath = "./test/testExtraction.txt"
        actualValue = getApiKeyFromFile(filePath)
        expectedValue = "helloWorldExtraction1289"
        self.assertEqual(actualValue, expectedValue, "Key extracted correctly")

if __name__ == '__main__':
    unittest.main()
