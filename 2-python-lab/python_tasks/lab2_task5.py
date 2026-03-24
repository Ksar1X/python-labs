ptk = int(input("Count of ptk: "))

if ptk > 7:
    proc = (ptk*100)/15
    match ptk:
        case 8:
            print(f"3.0 ({proc:.2f}%)")
        case 9:
            print(f"3.0 ({proc:.2f}%)")
        case 10:
            print(f"3.5 ({proc:.2f}%)")
        case 11:
            print(f"4.0 ({proc:.2f}%)")
        case 12:
            print(f"4.0 ({proc:.2f}%)")
        case 13:
            print(f"4.5 ({proc:.2f}%)")
        case 14:
            print(f"5.0 ({proc:.2f}%)")
        case 15:
            print(f"5.0 ({proc:.2f}%)")
else:
    print("Exam failed")
