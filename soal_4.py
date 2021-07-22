def reverse(kalimat):
    return kalimat[::-1]

if __name__ == '__main__':
    print("Program Reverse Kalimat")
    kalimat = input("Input kalimat: ")
    print(kalimat + " => " + reverse(kalimat))