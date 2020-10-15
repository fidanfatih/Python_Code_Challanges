import base64
from math import log,ceil
import base64Methods

string="İSTİKLAL MARŞI"
print(f"'{string}' is equal to '{base64Methods.stringToBase64(string)}' as base64.\n")

base64String="UHl0aG9uIGlzIGF3ZXNvbWU="
print(f"'{base64String}' is equal to '{base64Methods.base64ToString(base64String)}' as text.\n")

number=155628
print(f"'{number}' is equal to '{base64Methods.numberToBase64(number)}' as base64.\n")

numberAsBase64= "7F8C"
print(f"'{numberAsBase64}' is equal to '{base64Methods.base64ToNumber(numberAsBase64)}' as integer.\n")