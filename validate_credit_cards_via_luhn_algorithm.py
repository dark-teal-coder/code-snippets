def remove_spaces_hyphens(card_num): 
    card_num = card_num.replace(" ", "")
    card_num = card_num.replace("-", "")
    return card_num

def luhn_algo(card_num):
    digits = len(card_num)
    sum = 0
    every_2nd_digit = False
    
    for i in range(digits - 1, -1, -1):
        d_num = int(card_num[i])
        
        if (every_2nd_digit == True):
            d_num = d_num * 2
 
        ## If only 1 digit, add it to "sum". If 2 digits, add the sum of them to "sum".
        sum += d_num // 10
        sum += d_num % 10
        
        every_2nd_digit = not every_2nd_digit
    
    ## Check if the sum is a multiple of 10.
    if (sum % 10 == 0):
        return True
    else:
        return False

def check_validity(card_num):
    ## Check if the string contains only digits.
    if (card_num.isdigit() == False): 
        return "invalid"
    ## Check if the length is exactly 16.
    elif len(card_num) != 16:
        return "invalid"
    ## Apply Luhn algorithm. 
    elif (luhn_algo(card_num)):
        return "valid"
    else:
        return "invalid"

if __name__ == "__main__": 
    ## Force the user to input only an integer between 1 and 100.
    while True:
        try: 
            num_of_cards = int(input("Number of credit cards (1 to 100): "))
            if 1 <= num_of_cards <= 100:
                break
            else:
                print("Please enter a whole number between 1 and 100.")
        except ValueError:
            print("Number of credit cards must be a whole number.")
    card_validity = {}
    for i in range(num_of_cards):
        card_num = input("Please input your credit card number: ")
        card_num = remove_spaces_hyphens(card_num)
        card_validity[i] = check_validity(card_num)
    for i, validity in card_validity.items():
        print(f"Card {i+1}: {validity}")
