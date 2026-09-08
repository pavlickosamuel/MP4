fr = open("Subory/meteo_stanice.txt", "r", encoding = "utf-8")
fw = open("Subory/meteo_stanice_vystup.txt", "w", encoding = "utf-8")

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

fw.write(f"Počet meraní je: {counter}\n")
fw.write(f"Namerané teploty sú: {temperatures}\n")
fw.write(f"Najvyššia teplota je: {max(temperatures)} a bola nameraná na stanici {station}\n")
fw.write(f"Najvyššia teplota (ručne najdená) je: {max_temperature} a bola nameraná na stanici {station}\n")
fw.write(f"Priemerná teplota je: {round(sum(temperatures) / counter, 2)}\n")
fw.close()
