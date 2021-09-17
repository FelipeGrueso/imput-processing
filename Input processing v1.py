cadena = str()
while True:
    print("""Print a random string containing 0 or 1:
    """)
    entrada = input()
    for i in entrada:
        if i == "0" or i== "1":
            cadena = cadena + i
            
    if len(cadena) >= 100:
        print("Final data string:")
        print(cadena)
        break
    else:
        print(f"Current data length is {len(cadena)}, {100 - len(cadena)} symbols left")
    
