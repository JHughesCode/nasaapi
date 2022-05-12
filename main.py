import requests

print("""
   _       _                 _     _      ___      _            ___ _               _             
  /_\  ___| |_ ___ _ __ ___ (_) __| |    /   \__ _| |_ __ _    / __| |__   ___  ___| | _____ _ __ 
 //_\\/ __| __/ _ | '__/ _ \| |/ _` |   / /\ / _` | __/ _` |  / /  | '_ \ / _ \/ __| |/ / _ | '__|
/  _  \__ | ||  __| | | (_) | | (_| |  / /_/| (_| | || (_| | / /___| | | |  __| (__|   |  __| |   
\_/ \_|___/\__\___|_|  \___/|_|\__,_| /___,' \__,_|\__\__,_| \____/|_| |_|\___|\___|_|\_\___|_|   
                                                                                                 
Greetings Earthling. Welcome to the asteroid data checker."
This program provides data on all Near Earth Objects, or Asteroids, recorded by Nasa on a given date.""")
DATE = input("Please enter a date in format YYYY-MM-DD: ")
print("""Please wait...

""")

BASE_URL = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={DATE}&end_date={DATE}&api_key=CMGo2VZL52fcr7DKhiw5elgpUI64HNBOChw7noC8"
#BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2020-03-01&end_date=2020-03-07&api_key=CMGo2VZL52fcr7DKhiw5elgpUI64HNBOChw7noC8"
API_KEY = "CMGo2VZL52fcr7DKhiw5elgpUI64HNBOChw7noC8"

request_url = BASE_URL
response = requests.get(request_url)

NEODICT = {}

if response.status_code == 200:
    data = response.json()
    NEO = data["near_earth_objects"]
    NEODICT = NEO
else:
    print("Try again")

LISTNO = 0
for item in NEODICT[DATE]:
    NAME = item["name"]
    APPROACH_DATA = item["close_approach_data"]
    APPROACH_DATE = APPROACH_DATA[0]["close_approach_date"]
    ORBITING = APPROACH_DATA[0]["orbiting_body"]
    MAGNITUDE = item["absolute_magnitude_h"]
    VELOCITY = APPROACH_DATA[0]["relative_velocity"]["miles_per_hour"]
    MISS_DISTANCE = APPROACH_DATA[0]["miss_distance"]["miles"]
    if int(MAGNITUDE) <= 21 and float(MISS_DISTANCE) <= 4657698.4162491:
        HAZARD = True
    else:
        HAZARD = False
    if HAZARD is True:
        PREDICTION = ""
    else:
        PREDICTION = " NOT"
    LISTNO += 1
    print(f"""ASTEROID {LISTNO}:
This asteroid is named {NAME}, and is orbiting {ORBITING}.
It has an absolute magnitude of {MAGNITUDE}, and is travelling at {VELOCITY} miles per hour.
It IS{PREDICTION} predicted to coLlide with the Earth, with an expected miss distance of {MISS_DISTANCE} miles .
""")


print(NEODICT)

# root = Tk()
# root.title("Blah Blah Blah")
# root.geometry("400x400")
#
#
#
# # https://api.nasa.gov/neo/rest/v1/feed?start_date=2020-03-01&end_date=2020-03-07&api_key=CMGo2VZL52fcr7DKhiw5elgpUI64HNBOChw7noC8
#
# api_request = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2020-03-01&end_date=2020-03-07&api_key=CMGo2VZL52fcr7DKhiw5elgpUI64HNBOChw7noC8")
#
# try:
#     api = json.loads(api_request.content)
# except Exception as e:
#     api = "Error..."
#
# myLabel = Label(root, text=api["near_earth_objects"])
# myLabel.pack()
#
# root.mainloop()
#
# data =
#
# #
# # BASE_URL =