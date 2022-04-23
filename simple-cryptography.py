# Encryption and decryption using simple ciphers

# Setup

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def backwards(text): 
    # Reverses string
    result = ""
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    return result

def shift(text, amount = 1, direction = "left"): 
    # Shifts a string either left or right by a given number of characters
    if (direction.lower() == "left") or (direction.lower() == "l"):
        modifier = amount
    elif (direction.lower() == "right") or (direction.lower() == "r"):
        modifier = 0 - amount
    else:
        print("Direction not recognized. Defaulting to left.")
        modifier = amount
    
    new_string = ""
    for index in range(len(text)):
        new_string += text[(index + modifier) % len(text)]

    return new_string


# Cipher types

def caesar(message, shift_amt = 1, direction = "left"):
    # Cipher using shifted alphabet
    shifted_alphabet = shift(alphabet, shift_amt, direction)
    message = message.upper()
    result = ""

    for char in message:
        if char in alphabet:
            result += shifted_alphabet[alphabet.index(char)]
        else:
            result += char
    
    return result

def atbash(message):
    # Cipher using reversed alphabet
    backwards_alphabet = backwards(alphabet)
    message = message.upper()
    result = ""

    for char in message:
        if char in alphabet:
            result += backwards_alphabet[alphabet.index(char)]
        else:
            result += char

    return result


# Extras

def brute_force_caesar(message):
    # Et tu, Brute (force)?
    for shift_amt in range(26):
        print("Shift: left,", shift_amt)
        print(caesar(message, shift_amt),"\n")


brute_force_caesar("caesar test.")

# Ideas for future functions:
# - Polyalphabetic ciphers
# - Polygraphic substitution
# - One-time pad