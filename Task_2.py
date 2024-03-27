number = int(input())
numerals = ""

if 1 <= number < 10 and (number != 4 and number != 9 and number != 10):
    numerals = "V"
    numerals = numerals + ("I" * (number - 5))
    
    print(numerals)

elif number == 10:
    numerals = "X"

    print(numerals)

elif number == 4:
    numerals = "IV"

    print(numerals)

elif number == 9:
    numerals = "IX"

    print(numerals)