def input_bil():
    while True:
        try:
            bil = int(input("Input bilangan: "))
        except ValueError:
            print("Bukan bilangan, coba lagi...")
            continue
        else:
            break
    return bil

def hello_world(bil):
    cetak = "Output: "
    if bil%3==0:
        cetak += "Hello "
    if bil%5==0:
        cetak += "World"
    else:
        cetak+="None."
    return cetak

if __name__ == '__main__':
    print("Program Case 1 - Hello World.")
    bil = input_bil()
    print("Output: " + hello_world(bil))