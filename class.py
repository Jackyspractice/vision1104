from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Replace with valid values
ENDPOINT = "https://visionclass1104-prediction.cognitiveservices.azure.com"
prediction_key = "972c7db868514889afbfcebed253dda8"
project_id = "f3ee0ab0-8f4b-4157-b203-8e451237279f"
publish_iteration_name = "person_monkey"

# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

with open("C:\\Users\\B06-12\\Desktop\\work\\downloads\\test\\test.jpg", "rb") as image_contents:
    results = predictor.classify_image(
        project_id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))