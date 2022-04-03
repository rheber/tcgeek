from shared import loadJson, saveUrlToFile

def cardsUrl(banlist="tcg"):
    return "https://db.ygoprodeck.com/api/v7/cardinfo.php?banlist={}&sort=name".format(banlist)

def saveCardsToFile(banlist="tcg"):
    saveUrlToFile(cardsUrl(banlist), "yugioh-{}.json".format(banlist))

def getCardImageUrl(card):
    return card["card_images"][0]["image_url"]

#saveCardsToFile()
#cards = loadJson("yugioh-tcg.json")["data"]
#for card in cards:
#    saveUrlToFile(getCardImageUrl(card), "yugioh/{}-{}.jpg".format(card["id"], card["name"]), "wb")
