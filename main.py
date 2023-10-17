def convert_kg(value):
	# convert kg to lbs and oz
    oz = str(value * 35.274)
    lb = str(value * 2.20462)
    value = str(value)
    print(value + " kilograms = " + oz +" ounces")
    print(value + " kilograms = " + lb +" pounds")



def convert_pounds(value):
	# convert lbs to kg and oz
    kg = str(value * .453592)
    oz = str(value * 16)
    value = str(value)
    print(value + " pounds = "+kg+" kilograms")
    print(value+ " pounds = "+oz+" ounces")
    
def convert_ounces(value):
	# convert oz to kg and lbs
    kg = str(value * .0283)
    lb = str(value * .0625)
    value = str(value)
    print(value + " ounces = "+kg+" kilograms")
    print(value + " ounces = "+lb+" pounds")

convert_kg(10)
convert_pounds(10)
convert_ounces(10)

print("i was here")
