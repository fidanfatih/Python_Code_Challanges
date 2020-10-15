"""
https://edabit.com/challenge/uPAmqwiHmvwpwoBom

Roman Numeral Converter
Create a function that takes an Arabic number and converts it into a Roman number.

Examples
convert_to_roman(2) ➞ "II"

convert_to_roman(12) ➞ "XII"

convert_to_roman(16) ➞ "XVI"
Notes
All roman numerals should be returned as uppercase.
The largest number that can be represented in this notation is 3,999.
"""

def convert_to_roman ( num ) :
    roman = 'col' * (num // 1000)
    roman += 'C' * (num % 1000 // 100)
    roman += 'X' * (num % 100 // 10)
    roman += 'I' * (num % 10 // 1)
    roman = roman.replace ( 'C' * 9, 'CM' )
    roman = roman.replace ( 'C' * 5, 'D' )
    roman = roman.replace ( 'C' * 4, 'CD' )
    roman = roman.replace ( 'X' * 9, 'XC' )
    roman = roman.replace ( 'X' * 5, 'L' )
    roman = roman.replace ( 'X' * 4, 'XL' )
    roman = roman.replace ( 'I' * 9, 'IX' )
    roman = roman.replace ( 'I' * 5, 'V' )
    roman = roman.replace ( 'I' * 4, 'IV' )
    return roman


print ( convert_to_roman( int ( input ( "Enter a number(1-3999): " ) ) ) )
