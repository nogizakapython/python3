dict1 = {
        "Kyoko":"B",
        "Rio":"O",
        "Tsubame":"AB",
        "KurodaSensei":"A",
        "NekoSensei":"A"
        }

for item in dict1.items():
    array1 = list(item)
    key = array1[0]
    value = array1[1]

    print(key + " " + value)
