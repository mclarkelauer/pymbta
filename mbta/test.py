import urllib2
import mbta
import unittest

apiKey = "SLoajHTNgUCGBAN620QNbg" # Put Api Key Here

class baseTestCase(unittest.TestCase):
  def setUp(self):
    self.mbtaHandle = mbta.mbta(apiKey)

class badKeyTest(unittest.TestCase):
  def setUp(self):
    self.mbtaHandle = mbta.mbta("")

  def test_badApiKey(self):
    self.assertRaises(urllib2.HTTPError,lambda: self.mbtaHandle.routes())

class singleRequestTests(baseTestCase):
  def test_routes(self):
    

if __name__ == '__main__':
  unittest.main()
    
