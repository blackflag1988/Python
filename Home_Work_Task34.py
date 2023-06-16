# Задача 34

def rifm(data):
    lines = data.split()
    line = [line.split("-") for line in lines]
    words = [''.join(frag) for frag in line]

    simvol_count = [sum(1 for i in word if i == 'а') for word in words]
    simvol_count_first = simvol_count[0]

    for i in simvol_count:
        if simvol_count_first != simvol_count[1:]:
            return 'Парам пам-пам'
    else:
        return 'Пам парам'
    
data = "пара-ра-рам рам-пам-папам па-ра-па-да"
print(rifm(data))