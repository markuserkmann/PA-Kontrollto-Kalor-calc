"""Simple calculator script using different formulas for calculating the calories needed daily based on the user needs."""
import random

# Dictionary for storing the calories based on the food item
food_calories = {
    "Leib": 250,
    "Sai": 290,
    "Piim (2,5%)": 50,
    "Kohv (must, ilma suhkruta)": 2,
    "Must tee (ilma suhkruta)": 1,
    "Juust": 350,
    "Vorst": 300,
    "Või": 720,
    "Muna": 155,
    "Suhkur": 400,
    "Müsli": 370,
    "Kartul": 85,
    "Makaronid (keedetud)": 110,
    "Värske kurk": 15,
    "Värske tomat": 20,
    "Marineeritud kurk": 30,
    "Marineeritud kapsas": 20,
    "Šokolaad": 530,
    "Riis": 130,
    "Tatar": 340,
    "Seamaks": 135,
    "Rõskkoor": 200,
    "Praetud muna": 200,
    "Viinerid": 270,
    "Peekon": 500,
    "Uba tomatikastmes": 90,
    "Jäätis": 200,
}


def StartScript() -> None:
    """Initalizes the script, displays the info about the script and asks the user if they want to continue."""
    print("Tere tulemast PA Kalkulaatori. Kalkulaator on mõeldud kasutamiseks kõigile. Programm kalkuleerib välja teie enegriavajaduse, et hinnata kui palju kaloreid teie keha päevas vajab kehakaalu hoidmiseks, kaotamiseks või suurendamiseks. Programm on loodud Prait Kirilo ja Markus Erkmanni poolt.")
    Confirmation = input("Kas soovite jätkata? y/n \n").lower()
    if Confirmation == "y":
        AskInfoAboutTheUser()
    elif Confirmation == "n":
        return
    
def AskInfoAboutTheUser() -> None:
    """If the user confirms their choice the script asks the info needed for calculating"""    
    userAge = int(input("Palun sisestage enda vanus aastates \n")) # INT
    userSex = input("Palun sisetage enda sugu (m/n) \n").lower() # str
    userBW = int(input("Palun sisetage enda kaal kilodes \n")) # int
    userHeight = int(input("Palun sisestage enda pikkus sentimeetrites \n")) # int
    userPlan = input("Palun sisestage enda eesmärk antud kujul: \n Kui soovite kaalu kaotada sisetage - kaotus \n Kui soovite kaalu tõsta sisestage - tosta \n Kui soovite kaalu hoida sisestage - hoia \n").lower() # str
    userActivity = int(input("Palun sisestage enda kehaline aktiivsus antud kujul: \n istuv eluviis - 1 \n Väike aktiivsus - 2 \n Mõõdukas aktiivsus - 3 \n Kõrge aktiivsus -4 \n Väga kõrge aktiivsus - 5 \n"))

    StartCalculating(userAge, userSex, userBW, userHeight, userPlan, userActivity)

def StartCalculating(userAge: int, userSex: str, userBW: int, userHeight: int, userPlan: str, userActivity: str) -> None:
    """Starts the calculation process based on the info given.""" 
    Activity = {1:1.2, 2:1.375, 3:1.55, 4:1.725, 5:1.9}
    if userSex == "m":
        BMR = 88.36 + (13.4 * userBW) + (4.8 * userHeight) - (5.7 * userAge)
    else:
        BMR = 447.6 + (9.2 * userBW) + (3.1 * userHeight) - (4.3 * userAge)

    if BMR:
        Pal = Activity[userActivity]
        if userPlan == "kaotus":
            energy = (BMR * Pal) - 500
        elif userPlan == "tosta":
            energy = (BMR * Pal) - 300
        else:
            energy = BMR * Pal
        
        print(f"Kaloreid vaja päevas tarbida: {round(energy, 0)}")
        if input("Kas soovid abi toitumis valikuga? y/n \n").lower() == "y":
            help = HelperFunction(int(energy))
            print("Võiksid tarbida neid toiduaineid: \n")
            for i in help:
                print(f"Toit: {i[0]} ja annab kaloreid {i[1]}")
            return
        else:
            return

def HelperFunction(energy: int) -> tuple:
    """Picks random foods and makes their calories match the energy needed daily. Returns them as a tuple"""
    """:return: Returns the selected foods with their calories as a tuple"""
    total_calories = 0
    selected_foods = []
    
    foods = list(food_calories.items())
    
    while total_calories <= energy and foods:
        food, calories = random.choice(foods)
        if total_calories + calories <= energy:
            selected_foods.append((food, calories))
            total_calories += calories
        foods.remove((food, calories))
    
    return tuple(selected_foods)


# Initalizes the script
StartScript()