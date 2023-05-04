import csv
def main():
    f = open('q3.csv')
    data = csv.reader(f)
    header = next(data)
    station=[0,0,0,0,0,0,0,0,0]
    name=["1호선","2호선","3호선","4호선","5호선","6호선","7호선","8호선","9호선"]
    for row in data:
        row[4] = int(row[4])
        if(row[1]=="1호선"):
            station[0]=station[0]+row[4]
        if(row[1]=="2호선"):
            station[1]=station[1]+row[4]
        if(row[1]=="3호선"):
            station[2]=station[2]+row[4]
        if(row[1]=="4호선"):
            station[3]=station[3]+row[4]
        if(row[1]=="5호선"):
            station[4]=station[4]+row[4]
        if(row[1]=="6호선"):
            station[5]=station[5]+row[4]
        if(row[1]=="7호선"):
            station[6]=station[6]+row[4]
        if(row[1]=="8호선"):
            station[7]=station[7]+row[4]
        if(row[1]=="9호선"):
            station[8]=station[8]+row[4]
    
    for i in range(9):
        for j in range(i+1,9):
            if(station[i]<station[j]):
                tmp=station[i]
                station[i]=station[j]
                station[j]=tmp
                tmp=name[i]
                name[i]=name[j]
                name[j]=tmp

    print("***Subway Report for Seoul on March 2023***")
    print("1st Busiest Line : %s (%d)"%(name[0],station[0]))
    print("2nd Busiest Line : %s (%d)"%(name[1],station[1]))
    print("1st Least Used Line : %s (%d)"%(name[8],station[8]))
    print("2nd Least Used Line : %s (%d)"%(name[7],station[7]))


if __name__=="__main__":
    main()