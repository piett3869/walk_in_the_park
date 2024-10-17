
# %%
import geocoder

class Environment:
    def situation():
        g = geocoder.ip('me')
        latitude=g.lat
        longitude=g.lng
        """ from geopy.geocoders import Nominatim
        # initialize Nominatim API 
        geolocator = Nominatim(user_agent="geoapiExercises") """
        from geopy.geocoders import Photon
        geolocator = Photon(user_agent="measurements")
        location = geolocator.reverse(str(latitude)+","+str(longitude))
        city=location.address.split(",")[2]
        return city
    
class Input:
    def validation():
        while True:
            value = input("Do you want to stay in this city or leave?")
            try:
                value = value.lower()
            except ValueError:
                print("'Stay' or 'leave'?: ")
                continue
            if (value == "stay") | (value == "leave"):
                return value
            
            else:
                print("'Stay' or 'leave'?: ")

    def validation(question, repeat_question, options):
        while True:
            value = input(question)
            try:
                value = value.lower()
            except ValueError:
                print(repeat_question)
                continue
            if value in options:
                return value
            
            else:
                print(repeat_question)

class Ouput:
    def intro_to_new_area():
        print("You have been transported to an unknows area.")
        print("You are now standing in a dark forest;")
        print("To the north is a clearing, to the south is a dense thicket.")
            
# %%
city=Environment.situation()
print("You are in ",city,".")
response = Input.validation(
    question="Do you want to stay in this city or leave?",
    repeat_question="'Stay' or 'leave'?: ",
    options=["stay", "leave"]
)
# response="stay"
if response=="stay":
    print("You choose to stay...")
if response=="leave":
    Ouput.intro_to_new_area()
    direction=Input.validation(
        question="What do you do?",
        repeat_question="You can only go 'north' or 'south'",
        options=["north", "south"]
    )
    if direction=="north":

# %%
print("What do you do?")

# %%

""" 
> go north

You enter a clearing. There is a small stream to the west and a large oak tree to the east.

What do you do? > take acorn

You picked up an acorn.

What do you do? > go east

You approach the large oak tree. There is a small wooden chest at the base of the tree.

What do you do? > open chest

You opened the chest. Inside you find a key.

What do you do? > go south") """