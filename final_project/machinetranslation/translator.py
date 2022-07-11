"""this program translate text from french to english andverse versa"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version="2018-05-01",authenticator=authenticator)
language_translator.set_service_url(url)
def englishtofrench(entext):
    """translate to french"""
    frtext = language_translator.translate(text=entext,model_id="en-fr").get_result()
    return frtext.get("translations")[0].get("translation")
def frenchtoenglish(fretext):
    """translate to english"""
    enetext = language_translator.translate(text=fretext,model_id="fr-en").get_result()
    return enetext.get("translations")[0].get("translation")
#this is the end of the program    