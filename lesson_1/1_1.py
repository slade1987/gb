 duration = int(input("Введите число"))
    if (duration >= 86400):
        d = duration // 86400
        h = 0
        m = 0
        s = 0
        if ( (duration % 86400) >= 3600):
            h = (duration % 86400) // 3600
            if (((duration % 86400) % 3600) >= 60):
                m = ((duration % 86400) % 3600) // 60
                s = ((duration % 86400) % 3600) % 60
        elif((duration % 86400) >= 60):
            h = 0
            m = (duration % 86400) // 60
            s = (duration % 86400) % 60
        else:
            s = duration - 86400
        print(str(d) + " день " + str(h) + " час " + str(m) + " мин " + str(s) + " сек ")

    elif(duration >= 3600):
        h = duration // 3600
        s = duration % 3600
        m = 0
        if (s >= 60):
            m = s // 60
            s = s % 60
        print(str(h) + " час " + str(m) + " мин " + str(s) + " сек ")

    elif(duration >= 60):
        if ( duration // 60 > 0):
            time = duration % 60
            time2 = duration // 60
            print(str(time2) + " мин " + str(time) + " сек ")

    else:
        print(str(duration) + " сек ")
