Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

preguntas = ["Q1) Do you like Dawn or Dusk?", "Q2) When I’m dead, I want people to remember me as:", "Q3) Which kind of instrument most pleases your ear?"]

respuestas1 = ["1) Dawn", "2) Dusk"]
respuestas2 = ["1) The Good", "2) The Great", "3) The Wise", "4) The Bold"]
respuestas3 = ["1) The violin", "2) The trumpet", "3) The piano", "4) The drum"]

#Pregunta 1
print(preguntas[0], "\n   ", respuestas1[0], "\n   ", respuestas1[1])
numero = int(input('Selecciona uno: '))
if numero == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif numero == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Entrada Incorrecta")
#Pregunta 2
print(preguntas[1], "\n   ", respuestas2[0], "\n   ", respuestas2[1], "\n   ", respuestas2[2], "\n   ", respuestas2[3])
numero = int(input('Selecciona uno: '))
if numero == 1:
    Hufflepuff += 1
elif numero == 2:
    Slytherin += 1
elif numero == 3:
    Ravenclaw += 1
elif numero == 3:
    Gryffindor += 1
else:
    print("Entrada Incorrecta")
#Pregunta 3
print(preguntas[2], "\n   ", respuestas3[0], "\n   ", respuestas3[1], "\n   ", respuestas3[2], "\n   ", respuestas3[3])
numero = int(input('Selecciona uno: '))
if numero == 1:
    Slytherin += 1
elif numero == 2:
    Hufflepuff += 1
elif numero == 3:
    Ravenclaw += 1
elif numero == 3:
    Gryffindor += 1
else:
    print("Entrada Incorrecta")

# print("Gryffindor: ", Gryffindor)
# print("Ravenclaw: ", Ravenclaw)
# print("Hufflepuff: ", Hufflepuff)
# print("Slytherin: ", Slytherin)

if Gryffindor >= 2:
    print("Entraste a: ¡Gryffindor!")
elif Ravenclaw >= 2:
    print("Entraste a: ¡Ravenclaw!")
elif Hufflepuff >= 2:
    print("Entraste a: ¡Hufflepuff!")
elif Slytherin >= 2:
    print("Entraste a: ¡Slytherin!")
else:
    print("XD")
