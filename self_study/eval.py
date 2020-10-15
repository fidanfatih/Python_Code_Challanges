def convert_to_decimal(perc):
    return [eval(i.replace('%','/100')) for i in perc]

print(convert_to_decimal(['45%', '32%', '97%','33%']))