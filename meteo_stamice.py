fr = open("Subory/meteo_stanice.txt", "r", encoding = "utf-8")

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








print(f"Počet meraní je: {counter}")
print(f"Teploty sú: {temperatures}")
print(f"Najvyššia teplota je: {max(temperatures)} a bola nameraná na stanici {station}")
print(f"Najvyššia teplota (ručne najdená) je: {max_temperature} a bola nameraná na stanici {station}")
print(f"Priemerná teplota je: {sum(temperatures) / counter}")