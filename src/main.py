import tweepy, threading, logging
from random import randint
import config.config as cfg
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
file_handler = RotatingFileHandler('../log/kamouloxbot.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

voyelle = "a", "e", "é", "ê", "è", "i", "o", "u", "y", "h"

verbs = open("../resources/verbs.txt", "r", encoding="utf-8")
male = open("../resources/male.txt", "r", encoding="utf-8")
feminine = open("../resources/feminine.txt", "r", encoding="utf-8")
adjectifMale = open("../resources/adjectifMale.txt", "r", encoding="utf-8")
adjectifFeminine = open("../resources/adjectifFeminin.txt", "r", encoding="utf-8")
nameFemale = open("../resources/prenomFemale.txt", "r", encoding="utf-8")
nameMale = open("../resources/prenomMale.txt", "r", encoding="utf-8")
nameStars = open("../resources/prenomStar.txt", "r", encoding="utf-8")

verbsLines = verbs.readlines()
maleLines = male.readlines()
feminineLines = feminine.readlines()
adjMaleLines = adjectifMale.readlines()
adjFemininLines = adjectifFeminine.readlines()
nameMaleLines = nameMale.readlines()
nameFemaleLines = nameFemale.readlines()
nameStarLines = nameStars.readlines()

# auth = tweepy.OAuthHandler(cfg.apiKey, cfg.apiSecret)
# auth.set_access_token(cfg.accessToken, cfg.accessTokenSecret)
#
# api = tweepy.API(auth)
# user = api.me()

# try:
#     api.verify_credentials()
#     logger.info("Authentication OK")
# except:
#     logger.warning("Error during authentication")
#

def generateVerb():
    randVerbs = randint(0, len(verbsLines) - 1)
    verb = verbsLines[randVerbs]

    if verb.startswith(voyelle):
        return "j\'" + verb.rstrip()
    else:
        return "je " + verb.rstrip()


def generateWord(withAdj):
    int = randint(0, 1)
    adj = ""

    if withAdj == 1 and int == 1:
        adj = " " + adjMaleLines[randint(0, len(adjMaleLines)) - 1].rstrip()
    elif withAdj == 0 and int == 0:
        adj = " " + adjFemininLines[randint(0, len(adjFemininLines)) - 1].rstrip()

    if int == 1:
        return " un " + maleLines[randint(0, len(maleLines)) - 1].strip() + adj
    else:
        return " une " + feminineLines[randint(0, len(feminineLines)) - 1].strip() + adj

def generateName():
    int = randint(0, 2)

    if int == 0:
        return " " + nameMaleLines[randint(0, len(nameMaleLines)) - 1].rstrip().capitalize()
    elif int == 1:
        return " " + nameFemaleLines[randint(0, len(nameFemaleLines)) - 1].rstrip().capitalize()
    else:
        return " " + nameStarLines[randint(0, len(nameStarLines)) - 1].rstrip()

def nameOrWord():
    int = randint(0, 1)

    if int == 0:
        return generateWord(randint(0, 1))
    else:
        return generateName()

def generateSentence():
    return generateVerb().capitalize() + nameOrWord() + " et " + generateVerb() + nameOrWord() + "."

def postTweet():
    # threading.Timer(3600.0, postTweet).start()
    for x in range(10):
        tweet = generateSentence()
        print(tweet)
    # api.update_status(tweet)
    # logger.info("@" + user.screen_name + " Tweet : \"" + tweet + "\" as been posted")

postTweet()
