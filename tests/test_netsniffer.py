import unittest
from util.phantomjs import netsniff


class TestNetSniffer(unittest.TestCase):
    """ Unit test for netsniff method."""
    def test_sniff_google(self):
        json = netsniff("http://www.google.com")
        #PhantomJS version used should be return within JSON
        assert "PhantomJS" in json

if __name__ == '__main__':
    unittest.main()