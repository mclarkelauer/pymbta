import urllib
import urllib2
import json

class mbta:
  def __init__(self,api_key):
    self.api_key=api_key
    self.site="http://realtime.mbta.com/developer/api/v2/"

  def pretty(self,d,indent=0):
    for key, value in d.iteritems():
      print '\t' * indent + str(key) +"\n"
      if isinstance(value, dict):
        self.pretty(value, indent+1)
      else:
        print '\t' * (indent+1) + str(value) + "\n"

  def __makeRequest(self,url,data={}):
    #set api key
    data["api_key"]=self.api_key
    data["format"]="json"
    params= urllib.urlencode(data)
    resp = urllib2.urlopen(url+ "?" + params)
    jsonData = json.load(resp)
    return jsonData

  def __getURL(self,queryName):
    # Possible add validation for queryName
    return (self.site+queryName)

  # Return dictionary of modes, with routes and names 
  def routes(self):
    url = self.__getURL("routes")
    response = self.__makeRequest(url)
    return response 

  def routesByStop(self, stop_id):
    url=self.__getURL("routesbystop")
    data['stop_id']=stop_id
    response = self.__makeRequest(url)
    return response

  def stopsByRoute(self,route):
    url=self.__getURL("stopsbyroute")
    data['route']=route
    response = self.__makeRequest(url)
    return response

  def stopsByLocation(self,lat,lon):
    url=self.__getURL("stopsbylocation")
    data['lat']=lat
    data['lon']=lon
    response = self.__makeRequest(url)
    return response

  def scheduleByStop(self):
    pass

  def scheduleByRoute(self):
    pass

  def scheduleByTrip(self):
    pass

  def predictionsByStop(self):
    pass

  def predictionsByRoute(self):
    pass

  def vehiclesByRoute(self):
    pass

  def predictionsByTrip(self):
    pass

  def vehiclesByTrip(self):
    pass

  def alerts(self):
    pass

  def alertsByRoute(self):
    pass

  def alertsByStop(self):
    pass

  def alertsById(self):
    pass

  def alertsHeaders(self):
    pass

  def alertHeadersByRoute(self):
    pass

  def alertHeadersByStop(self):
    pass

  def serverTime(self):
    pass
