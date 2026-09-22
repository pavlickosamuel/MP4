fr = open("meteo_stanice.txt", "r")

counter = 0
temperatures = []
max_temperature = -100
station = "" 

for row in fr:
    processed_row = row.strip().split(" ")
    temp = float(processed_row[3].replace(",", "."))
    temperatures.append(temp)
    if temp > max_temperature:
        max_temperature = temp
        station = processed_row[0]
    print(processed_row)
    counter += 1

print(f"Počet meraní je: {counter}\n")
print(f"Namerané teploty sú: {temperatures}\n")
print(f"Najvyššia teplota je: {max_temperature} a bola nameraná na stanici {station}\n")
print(f"Priemerná teplota je: {round(sum(temperatures) / counter, 2)}\n")

