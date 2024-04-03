#input
h = int(input("Ingrese la altura inicial (en metros): "))
rebotes = 0
altura_actual = h

#processing
while altura_actual >= h / 5:
        rebotes += 1
        altura_actual *= 0.9

#output
print("La pelota no alcanza a subir la quinta parte de la altura inicial en el rebote número:", rebotes)
