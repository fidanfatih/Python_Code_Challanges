data=float(input("Angle: "))
angle,time=[],[]
for h in range(24):
    for m in range(60):
        ang=abs( (h%12+m/60)*30-m*6 )
        angle.append(ang  if ang <180 else 360-ang)
        time.append(f"{str(h).zfill(2)}:{str(m).zfill(2)}")
print(*[t for t,a in zip(time,angle) if abs(a-data)<0.000001])