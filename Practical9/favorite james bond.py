
born_year=input("write your born year ")
def favorite_james_bond(born_year):
    james_bond={"Roger Moore": (1973, 1986),
        "Timothy Dalton": (1987, 1994),
        "Pierce Brosnan": (1995, 2005), 
        "Daniel Craig": (2006, 2021)}    #create a directory includes names and years
    for actor, (start_year, end_year) in james_bond.items():
        if    start_year<=int(born_year)+18<end_year :
            return f"Your favorite Bond actor is {actor}."
        
    return "no favorite Bond actor"    #choos the correct character
print(favorite_james_bond(born_year))



