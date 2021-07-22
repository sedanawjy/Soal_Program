def kvr_waktu(waktu):
    waktu = waktu.lower()
    konvert = waktu[0:2]
    result = ""
    if 'am' in waktu:
        if konvert == '12':
            konvert = int(konvert)-12
            konvert = str(konvert)
            konvert = "0" + konvert + waktu[2:5]
        else:
            konvert += waktu[2:5]
    if 'pm' in waktu:
        if konvert == '12':
            konvert += waktu[2:5]
        else:
            konvert = int(konvert)-12
            konvert = str(konvert)
            konvert = "0" + konvert + waktu[2:5]
    else:
        konvert = "Mohon sesuaikan dengan format"
    return konvert


if __name__ == '__main__':
    print("Program Konversi Waktu\nFormat: 'JJ:MM:DD PM'")
    waktu = input("Input waktu: ")
    print(waktu + " => " + kvr_waktu(waktu))