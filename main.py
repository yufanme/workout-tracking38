import requests
from datetime import datetime
import os

os.environ["APP_ID"] = "c6b4ae56"
os.environ["API_KEY"] = "3f5e05df4229b1e564870baaf9e47668"
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
print(APP_ID)
print(API_KEY)


GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 163
AGE = 30

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
add_row_point ="https://api.sheety.co/ceecbf3b3e374ffa88da8b446ee81ce6/myWorkouts/workouts"

BASIC_AUTH = "Basic ZmFueXU6c2hlZXR5aXNmdW4="


exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_json = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=exercise_headers, json=exercise_json)
data = response.json()


now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")
exercise_name = data["exercises"][0]["name"].title()
exercise_duration = data["exercises"][0]["duration_min"]
exercise_calories = data["exercises"][0]["nf_calories"]
sheet_name = "workout"
add_row_json = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": exercise_calories
    }
}

add_row_basicauth_header = {
    "Authorization": BASIC_AUTH
}

# sheet_response = requests.post(url=add_row_point, json=add_row_json, headers=add_row_basicauth_header)
sheet_response = requests.post(
  add_row_point,
  json=add_row_json,
  auth=(
      "fanyu",
      "sheetyisfun",
  )
)
print(sheet_response.text)
