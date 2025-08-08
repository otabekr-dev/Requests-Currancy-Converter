import requests

def main():
    while True:
        print('---------- Menu ----------\n')
        print("1. Dollarni so'mga o'tkazish")
        print("2. So'mni dollarga o'tkazish")
        print("3. Chiqish")

        choice = input('Menuni tanlang (1-3): ')

        if choice == '1':
            data = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/').json()
            kurs = float(data[0]['Rate'])

            amount = float(input('Dollar: '))
            result = kurs * amount
            print(f"So'm: {result}")

        elif choice == '2':
            data = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/').json()
            kurs = float(data[0]['Rate'])

            amount = float(input("So'm: "))
            result = amount / kurs
            print(f"Dollar: {result}")

        elif choice == '3':
            print("Dastur tugadi.")
            break

        else:
            print("Xato tanlov, qaytadan urinib ko'ring.")

main()
