
triadas = {"000":[0,0], "001":[0,0], "010":[0,0], "011":[0,0], "100":[0,0], "101":[0,0], "110":[0,0], "111":[0,0]} 
cadena = "01011"
cantidad_triadas = len(cadena) -2
print ("longitud de la cadena", len(cadena))
print("triadas", cantidad_triadas)
i= 0
while i < len(cadena) - cantidad_triadas :

    print(cadena[i:i+3])

    if cadena[i:i+3] in triadas:

        if cadena[i+4] == "0":
            triadas[cadena[i:i+3]][0] = triadas[cadena[i:i+3]][0] + 1
            
        if cadena[i+4] == "1":
            triadas[cadena[i:i+3]][1] = triadas[cadena[i:i+3]][1] + 1

    i +=1
    
for j in triadas:
    print(f"{j}: {triadas[j][0]} {triadas[j][1]}")
