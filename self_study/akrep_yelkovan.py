time = input ( "What time is it? (hh:mm): " )
hour = int ( time.split ( ':' ) [ 0 ] ) % 12
minute = int ( time.split ( ':' ) [ 1 ] )
ang = abs ( (hour + minute / 60) * 30 - minute * 6 )
print ( ang if ang < 180 else 360 - ang )


time = str(input("Saati HH:MM formatında giriniz:"))
hour = int(time[:time.rfind(":")])
minute = int(time[time.rfind(":")+1:])
angle = (minute * 11 - 60 * hour) / 2
if angle < 0 :
    print(angle * -1)
else:
    print(angle)