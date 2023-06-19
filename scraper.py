from bs4 import BeautifulSoup
import requests
import json

def getJSON():
    try:
        with open("website.json") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("JSON file not found")
        
def getBanksJSON(data):
    try:
        return data["banks"]
    except TypeError:
        print("Incorrect data type!")

def getAllPersonalAccounts(data):

    try:
        for bank in data:
            response = requests.get(bank["urls"]["home"])
            print(response.status_code)
    except:
        print("error")

if __name__ == "__main__":
    js = getJSON()
    banks = getBanksJSON(js)
    # print(banks)
    getAllPersonalAccounts(banks)
