from shared import loadJson, saveUrlToFile

def cardsUrl(setCode="ex", page=1):
    """URL to list all cards from a given set."""
    return "https://api.pokemontcg.io/v1/cards?set={}&page={}".format(setCode, page)

def saveCardsToFile(setCode="ex", page=1):
    saveUrlToFile(cardsUrl(setCode, page), "pokemon-{}-{}.json".format(setCode, page))

def getCardImageUrl(card):
    return card["imageUrl"]

#saveCardsToFile()
#cards = loadJson("pokemon-ex-1.json")["cards"]
#for card in cards:
#    saveUrlToFile(getCardImageUrl(card), "pokemon/{}-{}.png".format(card["id"], card["name"]), "wb")
