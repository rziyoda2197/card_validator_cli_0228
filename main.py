def luhn_check(card_number):
    digits = [int(d) for d in card_number]
    digits.reverse()

    total = 0
    for i, num in enumerate(digits):
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        total += num

    return total % 10 == 0


card = input("Enter 16-digit card number: ").strip()

if not card.isdigit() or len(card) != 16:
    print("Invalid card format.")
else:
    if luhn_check(card):
        print("Valid card number.")
    else:
        print("Invalid card number.")
