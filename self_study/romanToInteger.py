def parse_roman_numeral (roman: str) -> int:
    translations = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
    number = 0
    roman = roman.replace ( "IV", "IIII" ).replace ( "IX", "VIIII" )
    roman = roman.replace ( "XL", "XXXX" ).replace ( "XC", "LXXXX" )
    roman = roman.replace ( "CD", "CCCC" ).replace ( "CM", "DCCCC" )
    for char in roman:
        number += translations [ char ]
    return number


roman=input("Enter a roman n: ")
print(parse_roman_numeral(roman))