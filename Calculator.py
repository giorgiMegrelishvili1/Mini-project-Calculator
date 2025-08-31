import math
import os

HISTORY_FILE = "history.txt"

# 👇 პირველი ყველა ფუნქცია
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "შეცდომა: ნულზე გაყოფა შეუძლებელია!"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "შეცდომა: უარყოფითიდან ფესვი არ გამოითვლება!"
    return math.sqrt(a)

def logarithm(a, base=10):
    if a <= 0:
        return "შეცდომა: ლოგარითმის არგუმენტი უნდა იყოს > 0"
    return math.log(a, base)

def save_history(expression, result):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{expression} = {result}\n")

def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("ისტორია ცარიელია.")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        print("\n--- კალკულატორის ისტორია ---")
        print(f.read())
        print("--------------------------\n")

# 👇 მერე მოდის მთავარი ფუნქცია
def calculator():
    while True:
        print("\n📌 აირჩიე ოპერაცია:")
        print("1. მიმატება (+)")
        print("2. გამოკლება (-)")
        print("3. გამრავლება (*)")
        print("4. გაყოფა (/)")
        print("5. ხარისხში აყვანა (x^y)")
        print("6. კვადრატული ფესვი (√x)")
        print("7. ლოგარითმი (log)")
        print("8. ისტორიის ნახვა")
        print("9. გამოსვლა")

        choice = input("👉 შენი არჩევანი: ")

        if choice == "1":
            a = float(input("პირველი რიცხვი: "))
            b = float(input("მეორე რიცხვი: "))
            result = add(a, b)
            print("შედეგი:", result)
            save_history(f"{a} + {b}", result)

        elif choice == "2":
            a = float(input("პირველი რიცხვი: "))
            b = float(input("მეორე რიცხვი: "))
            result = subtract(a, b)
            print("შედეგი:", result)
            save_history(f"{a} - {b}", result)

        elif choice == "3":
            a = float(input("პირველი რიცხვი: "))
            b = float(input("მეორე რიცხვი: "))
            result = multiply(a, b)
            print("შედეგი:", result)
            save_history(f"{a} * {b}", result)

        elif choice == "4":
            a = float(input("პირველი რიცხვი: "))
            b = float(input("მეორე რიცხვი: "))
            result = divide(a, b)
            print("შედეგი:", result)
            save_history(f"{a} / {b}", result)

        elif choice == "5":
            a = float(input("რიცხვი: "))
            b = float(input("ხარისხი: "))
            result = power(a, b)
            print("შედეგი:", result)
            save_history(f"{a}^{b}", result)

        elif choice == "6":
            a = float(input("რიცხვი: "))
            result = square_root(a)
            print("შედეგი:", result)
            save_history(f"√{a}", result)

        elif choice == "7":
            a = float(input("რიცხვი: "))
            base = input("ლოგარითმის ფუძე (დააჭირე Enter თუ გინდა 10): ")
            if base == "":
                base = 10
            else:
                base = float(base)
            result = logarithm(a, base)
            print("შედეგი:", result)
            save_history(f"log_{base}({a})", result)

        elif choice == "8":
            show_history()

        elif choice == "9":
            print("გამოსვლა... ნახვამდის! 👋")
            break

        else:
            print("❌ არასწორი არჩევანი, სცადე თავიდან.")


# 👇 და ბოლოს პროგრამის გაშვება
calculator()
