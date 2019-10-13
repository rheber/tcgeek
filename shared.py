import json
import urllib.request

def getUrl(url, utf8=True):
    req = urllib.request.Request(url, headers = {"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        if utf8:
            return response.read().decode("utf-8")
        return response.read()

def saveUrlToFile(url, filename, mode="w"):
    with open(filename, mode) as outputFile:
        outputFile.write(getUrl(url, mode == "w"))

def loadJson(filename):
    with open(filename) as inputFile:
        return json.loads(inputFile.read())
