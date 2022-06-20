data = []

while True:
    user = input("masukkan angka: ")
    if user == "n":
        break
    data.append(int(user))

total = sum(data)
rata = total/len(data)
print("hasil rata-rata= ",rata)
