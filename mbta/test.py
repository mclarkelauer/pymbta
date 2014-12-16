import urllib2
import mbta
import unittest

apiKey = "SLoajHTNgUCGBAN620QNbg" # Put Api Key Here

class baseTestCase(unittest.TestCase):
  def setUp(self):
    self.mbtaHandle = mbta.mbta(apiKey)

class badKeyTestCase(unittest.TestCase):
  def setUp(self):
    self.mbtaHandle = mbta.mbta("")

  def test_badApiKey(self):
    self.assertRaises(urllib2.HTTPError,self.mbtaHandle.routes())

if __name__ == '__main__':
  unittest.main()
    
