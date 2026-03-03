def dollars_to_float(dollars):
    return float(dollars.replace("$", ""))
def percent_to_float(percent):
    return float(percent.replace("%", "")) / 100
def main():
    dollars = input("Yemek ne kadardı?")
    percent = input("Yüzde kaç bahşiş bırakmak istersiniz?")
    tip = dollars_to_float(dollars) * percent_to_float(percent)
    print(f"${tip:.2f}")
main()