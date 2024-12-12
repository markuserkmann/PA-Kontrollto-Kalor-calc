"""Simple calculator script using different formulas for calculating the calories needed daily based on the user needs."""

from tkinter import *
import csv
import random

def HelperFunction(energy: int) -> tuple:
    """Picks random foods and makes their calories match the energy needed daily. Returns them as a tuple"""
    """:return: Returns the selected foods with their calories as a tuple"""
    with open("toit_andmed.csv", mode="r", encoding="utf-8") as file:
        cFile = csv.reader(file)
        next(cFile)
        foods = [(row[0], int(row[1])) for row in cFile]

    total_calories = 0
    selected_foods = []

    while total_calories <= energy and foods:
        food, calories = random.choice(foods)
        if total_calories + calories <= energy:
            selected_foods.append((food, calories))
            total_calories += calories
        foods.remove((food, calories))

    return selected_foods 

def arvuta_bmr() -> None:
    """Function to calculate the kcal needed daily for a user."""
    try:
        kaal = float(kaal_entry.get()) #float
        pikkus = float(pikkus_entry.get()) #float
        vanus = int(vanus_entry.get()) #int
        sugu = sugu_var.get() #str
        aktiivsus_tase = aktiivsus_var.get() #str

        if sugu == "Mees":
            bmr = 88.36 + (13.4 * kaal) + (4.8 * pikkus) - (5.7 * vanus)
        else:
            bmr = 447.6 + (9.2 * kaal) + (3.1 * pikkus) - (4.3 * vanus)

        aktiivsus_kordaja = {
            "istuv eluviis": 1.2,
            "väike aktiivsus": 1.375,
            "mõõdukas aktiivsus": 1.55,
            "kõrge aktiivsus": 1.725,
            "väga kõrge aktiivsus": 1.9
        }

        bmr_aktiivsus = bmr * aktiivsus_kordaja[aktiivsus_tase]
        sel_food = HelperFunction(int(bmr_aktiivsus))

        stringt = ""
        for i in sel_food:
            stringt += f"Toit: {i[0]} ja kaloreid: {i[1]}, "

        tulemus_label.config(text=f"Päevane kalorivajadus: {round(bmr_aktiivsus)} kcal. Soovitatavad toidud mida tarbida: \n {stringt} ")
    except Exception as e:
        tulemus_label.config(text="Palun sisesta korrektsed andmed!")

# Praidi pooleldi tehtud GUI
raam = Tk()
raam.title("Kalorite Kalkulaator")
raam.geometry("400x600")
raam.configure(bg="lightblue")

pealkiri_label = Label(raam, text="BMR Kalkulaator", font=("Calibri", 16), bg="lightblue")
pealkiri_label.pack(pady=10)

kaal_label = Label(raam, text="Sisesta kaal (kg):", font=("Calibri", 12), bg="lightblue")
kaal_label.pack()
kaal_entry = Entry(raam)
kaal_entry.pack()

pikkus_label = Label(raam, text="Sisesta pikkus (cm):", font=("Calibri", 12), bg="lightblue")
pikkus_label.pack()
pikkus_entry = Entry(raam)
pikkus_entry.pack()

vanus_label = Label(raam, text="Sisesta vanus (1-100):", font=("Calibri", 12), bg="lightblue")
vanus_label.pack()
vanus_entry = Entry(raam)
vanus_entry.pack()

sugu_label = Label(raam, text="Sugu:", font=("Calibri", 12), bg="lightblue")
sugu_label.pack()
sugu_var = StringVar(value="Mees")
mees_radio = Radiobutton(raam, text="Mees", variable=sugu_var, value="Mees", font=("Calibri", 10), bg="lightblue")
mees_radio.pack()
naine_radio = Radiobutton(raam, text="Naine", variable=sugu_var, value="Naine", font=("Calibri", 10), bg="lightblue")
naine_radio.pack()

aktiivsus_label = Label(raam, text="Aktiivsuse tase:", font=("Calibri", 12), bg="lightblue")
aktiivsus_label.pack()
aktiivsus_var = StringVar(value="istuv eluviis")
aktiivsus_valik = OptionMenu(raam, aktiivsus_var, "istuv eluviis", "väike aktiivsus", "mõõdukas aktiivsus", "kõrge aktiivsus", "väga kõrge aktiivsus")
aktiivsus_valik.pack()

arvuta_nupp = Button(raam, text="Arvuta", font=("Calibri", 12), command=arvuta_bmr)
arvuta_nupp.pack(pady=12)

tulemus_label = Label(raam, text="", font=("Calibri", 12), bg="lightblue", wraplength=300, justify="center")
tulemus_label.pack(pady=10)

raam.mainloop()