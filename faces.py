def convert(cümle):
    cümle = cümle.replace(":)", "🙂")
    cümle = cümle.replace(":(", "🙁")
    return cümle
def main():
    metin = input("Bir metin girin: ")
    result = convert(metin)
    print(result)
main()