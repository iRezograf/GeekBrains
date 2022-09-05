def IsEven( x, y ):
    if (x%y == 0):
        print(f"{x}, {y} -> кратно|")
    else:
        print(f"{x}, {y} -> не кратно, остаток {x%y}")