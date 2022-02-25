import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)
    count = theJSON['metadata']['count']
    print(str(count) + " events recorded")

def printFeltPlaceMag(data):
    for i in data['features']:
        feltReport = i["properties"]["felt"]
        if feltReport != None and feltReport > 0:
            print("%2.1f" % i["properties"]["mag"], i['properties']['place'], 
            " reported " + str(feltReport) + " times")

def printTitle(data):
    if "title" in data["metadata"]:
        print(data["metadata"]["title"])

def printPlace(data):
    for i in data["features"]:
        print(i['properties']['place'])

    print("__________\n")

def printMag(data):
    for i in data['features']:
        if i['properties']['mag'] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i['properties']['place'])
    print("__________\n")


def main():

    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))

    if webUrl.getcode() == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, cannot parse results")


if __name__ == "__main__":
    main()