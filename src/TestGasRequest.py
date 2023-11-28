import unittest

import GasRequest as GR


class TestGasRequest(unittest.TestCase):
    def setUp(self):
        self.gas_request = GR.GasRequest()

    def test_new_pincode(self):
        pincode = self.gas_request.new_pincode()
        self.assertEqual(len(pincode), 4)

    def test_get_pincode(self):
        pincode = self.gas_request.new_pincode()
        self.assertEqual(self.gas_request.get_pincode(), pincode)

    def test_del_pincode(self):
        pincode = self.gas_request.new_pincode()
        self.assertEqual(self.gas_request.del_pincode(), pincode)

if __name__ == "__main__":
    unittest.main()