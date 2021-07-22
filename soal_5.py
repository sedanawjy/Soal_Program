def ini_palindrom(kalimat):
    return kalimat == kalimat[::-1]

if __name__ == '__main__':
    print("Program Reverse Kalimat")
    kalimat = input("Input kalimat: ")
    if ini_palindrom:
        print(kalimat + " di balik " + kalimat[::-1] + " => Result True")
    else:
        print(kalimat + " di balik " + kalimat[::-1] + " => Result False")