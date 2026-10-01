escribir = input("Introduce una palabra o frase en minúsculas sin signos de puntuación: ")

min = 0
max = len(escribir) - 1

palindromo = True

while min < max and palindromo:
    if escribir[min] != escribir[max]:
        palindromo = False
        break
    min = min +1
    max = max -1

if palindromo == True:
    print("Es palíndromo.")
else:
    print("No es palíndromo.")