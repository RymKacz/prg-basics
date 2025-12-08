def f(time1,time2):
    if ("pm" in time1 or "am" in time1):
        tablehelp1 = []
        tablehelp2 = []
        for char1 in time1:
            tablehelp1.append(char1)
        for char2 in time2:
            tablehelp2.append(char2)
        hh1 = int(tablehelp1[0])
        mm1 = int(tablehelp1[2] + tablehelp1[3])
        hh2 = int(tablehelp2[0] + tablehelp2[1])
        mm2 = int(tablehelp2[3] + tablehelp2[4])
        if("am" in time1):
            if(hh1 == hh2):
                if(mm1 < mm2):
                    return time1
                elif(mm1 > mm2):
                    return time2
                else:
                    return time1
            elif(hh1 < hh2):
                return time1
            else:
                return time2
        if("pm" in time1):
            if(hh1+12 == hh2):
                if(mm1 < mm2):
                    return time1
                elif(mm1 > mm2):
                    return time2
                else:
                    return time1
            elif(hh1+12 < hh2):
                return time1
            else:
                return time2
    elif("pm" in time2 or "am" in time2):
        tablehelp1 = []
        tablehelp2 = []
        for char1 in time1:
            tablehelp1.append(char1)
        for char2 in time2:
            tablehelp2.append(char2)
        hh1 = int(tablehelp1[0] + tablehelp1[1])
        mm1 = int(tablehelp1[3] + tablehelp1[4])
        hh2 = int(tablehelp2[0])
        mm2 = int(tablehelp2[2] + tablehelp2[3])
        if("am" in time2):
            if(hh1 == hh2):
                if(mm1 < mm2):
                    return time1
                elif(mm1 > mm2):
                    return time2
                else:
                    return time1
            elif(hh1 < hh2):
                return time1
            else:
                return time2
        if("pm" in time2):
            if(hh1 == hh2+12):
                if(mm1 < mm2):
                    return time1
                elif(mm1 > mm2):
                    return time2
                else:
                    return time1
            elif(hh1 < hh2+12):
                return time1
            else:
                return time2
    elif("pm" in time1 or "am" in time1 and "pm" in time2 or "am" in time2):
        tablehelp1 = []
        tablehelp2 = []
        for char1 in time1:
            tablehelp1.append(char1)
        for char2 in time2:
            tablehelp2.append(char2)
        hh1 = int(tablehelp1[0])
        mm1 = int(tablehelp1[2] + tablehelp1[3])
        hh2 = int(tablehelp2[0])
        mm2 = int(tablehelp2[2] + tablehelp2[3])
        if("am" in time1):
            if(hh1 == hh2):
                if(mm1 < mm2):
                    return time1
                elif(mm1 > mm2):
                    return time2
                else:
                    return time1
            elif(hh1 < hh2):
                return time1
            else:
                return time2
        if("pm" in time1):
            if(hh1 == hh2):
                if(mm1 < mm2):
                    return time1
                elif(mm1 > mm2):
                    return time2
                else:
                    return time1
            elif(hh1 < hh2):
                return time1
            else:
                return time2
    else:
        tablehelp1 = []
        tablehelp2 = []
        for char1 in time1:
            tablehelp1.append(char1)
        for char2 in time2:
            tablehelp2.append(char2)
        hh1 = int(tablehelp1[0] + tablehelp1[1])
        mm1 = int(tablehelp1[3] + tablehelp1[4])
        hh2 = int(tablehelp2[0] + tablehelp2[1])
        mm2 = int(tablehelp2[3] + tablehelp2[4])
        if(hh1 == hh2):
            if(mm1 < mm2):
                return time1
            elif(mm1 > mm2):
                return time2
            else:
                return time1
        elif(hh1 < hh2):
            return time1
        else:
            return time2
if __name__  == "__main__":
    print(f("13:06","13:12"))
    print(f("1:38pm","13:31"))
    print(f("08:08","8:01am"))
    print(f("6:00pm","18:00"))