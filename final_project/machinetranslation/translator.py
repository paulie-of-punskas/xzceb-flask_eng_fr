import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
import requests 

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# === create IBM Watson Language translator instance ===================================
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

# define englishToFrench method ========================================================
def englishToFrench(englishText):
    serverReturn = language_translator.translate(text=str(englishText),
    source="en", 
    target="fr").get_result()
    englishText = serverReturn['translations'][0]['translation']
    return englishText

# define frenchToEnglish method ========================================================
def frenchToEnglish(frenchText):
    serverReturn = language_translator.translate(text=str(frenchText),
    source="fr", 
    target="en").get_result()
    frenchText = serverReturn['translations'][0]['translation']
    return frenchText


