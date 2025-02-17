EGG = 6.4
CHICKEN_BREAST = 34.8
SIRLOIN_STEAK = 49.0
WHOLE_MILK = 3.5 #100ml
HALF_PACK_OF_PRAWNS = 13.8
BEEF_JERKY = 27
PORK_SAUSAGE = 8.7
BACON = 5.6

#Body mass in kg
BODY_MASS = 94.4

def convert_kg_to_lb(mass_kg):
    return round(mass_kg * 2.2, 1)

mass_lb = convert_kg_to_lb(BODY_MASS)
print(f"{mass_lb} grams")