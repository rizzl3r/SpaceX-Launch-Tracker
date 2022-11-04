from pip._vendor import requests
import time
def load_site():
    global site_latest, site_next, site_upcoming

    site_latest = None
    site_next = None
    site_upcoming = None

    try:
        site_latest = requests.get("https://ll.thespacedevs.com/2.2.0/launch/previous/?limit=1&search=spaceX")
        site_next = requests.get("https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=2&search=spaceX")
        site_upcoming = site_next # For the time being, recycle the API call since LL2API seems to be inclusive on the results AND we only get 15 API calls an hour.
        did_work = True
    except Exception as e:
        print(e)
        did_work = False
    while did_work == False:
        try:
            while site_latest == "None" or site_latest == None or site_next == "None" or site_next == None or site_upcoming == "None" or site_upcoming == None:
                site_latest = requests.get("https://ll.thespacedevs.com/2.2.0/launch/previous/?limit=1&search=spaceX")
                site_next = requests.get("https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=2&search=spaceX")
                site_upcoming = site_next
                print("ERROR OCCURED")
            did_work = True
        except:
            print("ERROR OCCURED")
            time.sleep(60)
            did_work = False
    site_latest = site_latest.json()
    site_next = site_next.json()
    site_upcoming = site_upcoming.json()

def latest_launch(info_to_get="name", number=0):
    global site_latest, site_next, site_upcoming
    return site_latest["results"][number][info_to_get]
def next_launch(info_to_get="details", number=0):
    global site_latest, site_next, site_upcoming
    return site_next["results"][number]["mission"][info_to_get]
def next_launch_meta(info_to_get="net", number=0):
    global site_latest, site_next, site_upcoming
    return site_next["results"][number][info_to_get]
# def next_launch_core(info_to_get="gridfins"): #Removing, LL2API doesn't seem to support this
#     global site_latest, site_next, site_upcoming
#     return site_next["cores"][info_to_get]
def get_more_launches(info_to_get="name", number=1):
    global site_latest, site_next, site_upcoming
    return site_upcoming["results"][number]["mission"][info_to_get]
def next_launch_location(info_to_get="name", number=0):
    global site_latest, site_next, site_upcoming
    return site_next["results"][number]["pad"]["location"][info_to_get]
def next_launch_pad(info_to_get="name", number=0):
    global site_latest, site_next, site_upcoming
    return site_next["results"][number]["pad"][info_to_get]
