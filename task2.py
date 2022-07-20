value = int(input("Insert the value to be converted: "))
intention = input("Type H to convert it from hours to minutes or M to do the opposite: ")

if intention == "H" or "h":
    print("Such value is equivalent to", value*60, "minutes")
else:
    print("Such value is equivalent to", value/60, "hours")


