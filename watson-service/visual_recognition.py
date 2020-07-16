import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('QvghErM7FRLWNPu7kTkVsNsnEyfaCr9Zu_20_UQ-tDtR')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/'+ config.api_key)

def classify_image(image_url):

    url = image_url
    classes = visual_recognition.classify(url=url, classifier_ids=["surfaces_800290789"]).get_result()

    covid_lifetime = {"paper": "3 hours", "cardboard": "24 hours", "wood": "2 days", "": "unable to give estimate as surface was not identified"}

    cleaning_advice = {"paper": "dispose of safely", "cardboard": "dispose of safely", "wood": "clean with 1:499 parts bleach to water, allowing to air dry afterwards", "": "unable to give advice - surface not identified"}

    class_name = ((((((((classes)["images"])[0])["classifiers"])[0])["classes"])[0])["class"])

    return {'surface_name': class_name, 'life_time': covid_lifetime[class_name], 'advice': cleaning_advice[class_name]}

