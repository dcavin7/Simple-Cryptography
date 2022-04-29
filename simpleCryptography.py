# Encryption and decryption using simple ciphers

# Setup

import math
import numpy as np

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def backwards(text): 
    """Reverses a string."""
    result = ""
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    return result

def shift(text, amount = 1, direction = "left"): 
    """Shifts a string either left or right by a given number of characters."""
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

# CIPHER TYPES

# Substitution ciphers

def caesar(message, shift_amt = 1, direction = "left"):
    """Substitution cipher using shifted alphabet."""
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
    """Substitution cipher using reversed alphabet."""
    backwards_alphabet = backwards(alphabet)
    message = message.upper()
    result = ""

    for char in message:
        if char in alphabet:
            result += backwards_alphabet[alphabet.index(char)]
        else:
            result += char

    return result

# Transposition ciphers

def scytale(message, encrypt = True, chars_around = 4, print_matrix = False):
    """Transposition cipher. Simulates writing on a strip of parchment
    wound around a rod, then reading the parchment after it is unwound."""

    # WORK IN PROGRESS

    message = message.upper()

    message_length = len(message)
    if encrypt == True:
        num_rows = chars_around
        num_cols = math.ceil(message_length/chars_around)
    else:
        num_cols = chars_around
        num_rows = math.ceil(message_length/chars_around)
    
    text_matrix = np.empty((num_rows, num_cols), dtype = "object")
    
    for j in range(num_rows):
        for i in range(num_cols):
            try:
                text_matrix[j, i] = message[(j*num_cols) + i]
            except IndexError:
                text_matrix[j, i] = ""

    if print_matrix == True:
        print(text_matrix)
    
    result_string = ""

    for j in range(num_cols):
        for i in range(num_rows):
            result_string += text_matrix[i, j]

    return result_string

# Extras

def brute_force_caesar(message):
    """Runs a string through all possible Caesar cipher shifts."""
    # Et tu, Brute (force)?
    bfc_result = ""
    for shift_amt in range(26):
        bfc_result += "Shifted left, "
        bfc_result += str(shift_amt)
        bfc_result += ": "
        bfc_result += caesar(message, shift_amt)
        bfc_result += "\n"
    return bfc_result

# Tests - Uncomment as needed
# print(atbash("test"))
# print(caesar("test"))
# print(brute_force_caesar("test"))
# print(scytale("this is a test"))



# Ideas for future functions:
# - Polyalphabetic ciphers
# - Polygraphic substitution
# - One-time pad