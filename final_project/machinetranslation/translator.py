import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

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


def englishToFrench(english_text=""):
    if english_text == "":
        french_text = "Input parameter cannot be empty"
    else:
        server_return = language_translator.translate(text=str(english_text),
        source="en",
        target="fr").get_result()
        french_text = server_return['translations'][0]['translation']
    return french_text


def frenchToEnglish(french_text=""):
    if french_text == "":
        english_text = "Input parameter cannot be empty"
    else:
        server_return = language_translator.translate(text=str(french_text),
        source="fr",
        target="en").get_result()
        english_text = server_return['translations'][0]['translation']
    return english_text
