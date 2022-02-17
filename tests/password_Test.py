import unittest
from server.valid_for_pass import Password


class TestPassword(unittest.TestCase):

    def test_upper(self):
        self.assertFalse(Password.valid_pass("DDWADWAD"))
        self.assertFalse(Password.valid_pass("FEGJAWPOGFJ"))
        self.assertFalse(Password.valid_pass("DKAWDKAWKDAKPKFGGFWAGLAW'"))

    def test_lower(self):
        self.assertFalse(Password.valid_pass("wadawddwwad"))
        self.assertFalse(Password.valid_pass("afawfawf"))
        self.assertFalse(Password.valid_pass("awfaasssw"))

    def test_numbers(self):
        self.assertFalse(Password.valid_pass("213124124"))
        self.assertFalse(Password.valid_pass("568568568"))
        self.assertFalse(Password.valid_pass("028940148"))

    def test_symbols(self):
        self.assertFalse(Password.valid_pass("#$!@!%@%@!"))
        self.assertFalse(Password.valid_pass("^#@^#@^#@%$@#"))
        self.assertFalse(Password.valid_pass("&$%&#^#$^#$'"))

    def test_normal_pass(self):
        self.assertTrue(Password.valid_pass("ddawd12A$%@!a"))
        self.assertTrue(Password.valid_pass("DADWDA#$!24afafwawf"))
        self.assertTrue(Password.valid_pass("dwwrwq22!!!""@$#@$!D"))


if __name__ == "__main__":
    unittest.main()
