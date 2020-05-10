from boltiot import Bolt
import time

api_key = "44c0d2d6-e6f4-40e8-8b9d-dbc84f874c7e"    # your bolt api key
device_id  = "BOLT1115460"  #your bolt device id
mybolt = Bolt(api_key, device_id)

# morse code dictionary; source: https://en.wikipedia.org/wiki/Morse_code
morse_code_dict = {"A":"._", "B":"_...", "C": "_._.", "D": "_..", "E": ".", "F": ".._.",
                   "G": "__.", "H": "....", "I": "..", "J": ".___", "K": "_._", "L": "._..",
                   "M": "__", "N": "_.", "O": "___", "P": ".__.", "Q": "__._", "R": "._.",
                   "S": "...", "T": "_", "U": ".._", "V": "..._", "W": ".__", "X": "_.._",
                   "Y": "_..__", "Z": "__..", "1": ".____", "2": "..___", "3": "...__", "4": "...._",
                   "5": ".....", "6": "_....", "7": "__...", "8": "___..", "9": "____.", "0": "_____", " ": ""}

def list_to_string(s):  # helper function to convert list to string
    string = ""

    for letter in s:
        string += letter

    return string

def filtered_string(string):    # this function filter unnecessary symbols from the important message
    ignore = "~`!@#$%^&*()_+{}|[]\:'<>?,./';-="
    # converting to list because strings are immutable
    string = list(string)
    ignore = list(ignore)

    for i in range(len(string)):
        for j in range(len(ignore)):
            if string[i] == ignore[j]:
                string[i] = ""

    string = (list_to_string(string)).upper()

    return string

def morse_code_converter(string):   # function to convert main message to morse code
    string = filtered_string(string)
    morse_code = ""

    print("Filtered string: ", string)

    for i in string:
        morse_code = morse_code + morse_code_dict[i] + " "

    return morse_code

def led_blink(code):    # function to blink the led on bolt according to dits and dahs in morse code

# timing counts are according to the source: http://www.morsecodeclassnet.com/lesson3/
    for i in code:
        if i == ".":    # dit
            mybolt.digitalWrite('0', 'HIGH')
            time.sleep(0.1)
            mybolt.digitalWrite('0', 'LOW')

        elif i == "_":  #dah
            mybolt.digitalWrite('0', 'HIGH')
            time.sleep(0.3)
            mybolt.digitalWrite('0', 'LOW')

        elif i == " ":  # space between letters and words
            time.sleep(0.3)


string = input("Enter the string (type '-exit' to quit): ")

while string != "-exit":
    morse_code = morse_code_converter(string)
    print(morse_code)
    # led_blink(morse_code)

    string = input("Enter the string (type '-exit' to quit): ")