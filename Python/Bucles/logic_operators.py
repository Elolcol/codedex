hunger = 5
anger = 2
#El operador "and" se ejecuta si ambas condiciones son verdaderas. No se ejecuta de lo contrario
if hunger > 4 and anger > 1:
  print("Hangry")

coffee = 2
bubble_tea = 1
#El operador "or" se ejecuta si una de las dos condiciones son verdaderas. No se ejecuta de lo contrario
if coffee > 0 or bubble_tea > 0:
  print("☺️")

tired = False
#El operador "not" devuelve True si la condicion es False. Y al reves
if not tired:
  print("Let's code!")