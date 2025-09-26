def soma(x, y, z=None):
    if z is not None:
        print(f'{x=}+ y={y}+ z={z}','|','x + y + z =',x+y+z)
    else:
        print(f'{x=}+ y={y}','|','x + y ',x+y)
soma(1,2)
soma(1,2,3)