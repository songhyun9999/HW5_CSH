import csv
def main():
    f = open('q3.csv')
    data = csv.reader(f)
    header = next(data)
    Line1=[]
    Line1_name=[]
    Line2=[]
    Line2_name=[]
    Line3=[]
    Line3_name=[]
    Line4=[]
    Line4_name=[]

    for row in data:
        row[4] = int(row[4])
        if(row[1]=="1호선"):
            Line1.append(row[4])
            Line1_name.append(row[3])
        if(row[1]=="2호선"):
            Line2.append(row[4])
            Line2_name.append(row[3])
        if(row[1]=="3호선"):
            Line3.append(row[4])
            Line3_name.append(row[3])
        if(row[1]=="4호선"):
            Line4.append(row[4])
            Line4_name.append(row[3])
    
    for i in range(len(Line1)):
        for j in range(i+1,len(Line1)):
            if(Line1[i]<Line1[j]):
                tmp=Line1[i]
                Line1[i]=Line1[j]
                Line1[j]=tmp
                tmp=Line1_name[i]
                Line1_name[i]=Line1_name[j]
                Line1_name[j]=tmp
    for i in range(len(Line2)):
        for j in range(i+1,len(Line2)):
            if(Line2[i]<Line2[j]):
                tmp=Line2[i]
                Line2[i]=Line2[j]
                Line2[j]=tmp
                tmp=Line2_name[i]
                Line2_name[i]=Line2_name[j]
                Line2_name[j]=tmp
    for i in range(len(Line3)):
        for j in range(i+1,len(Line3)):
            if(Line3[i]<Line3[j]):
                tmp=Line3[i]
                Line3[i]=Line3[j]
                Line3[j]=tmp
                tmp=Line3_name[i]
                Line3_name[i]=Line3_name[j]
                Line3_name[j]=tmp
    for i in range(len(Line4)):
        for j in range(i+1,len(Line4)):
            if(Line4[i]<Line4[j]):
                tmp=Line4[i]
                Line4[i]=Line4[j]
                Line4[j]=tmp
                tmp=Line4_name[i]
                Line4_name[i]=Line4_name[j]
                Line4_name[j]=tmp

    print("***Subway Report for Seoul on March 2023***")
    print("Line 1:")
    print("Busiest Station : %s (%d)"%(Line1_name[0],Line1[0]))
    print("Least used Station : %s (%d)"%(Line1_name[len(Line1)-1],Line1[len(Line1)-1]))
    print("Line 2:")
    print("Busiest Station : %s (%d)"%(Line2_name[0],Line2[0]))
    print("Least used Station : %s (%d)"%(Line2_name[len(Line2)-1],Line2[len(Line2)-1]))
    print("Line 3:")
    print("Busiest Station : %s (%d)"%(Line3_name[0],Line3[0]))
    print("Least used Station : %s (%d)"%(Line3_name[len(Line3)-1],Line3[len(Line3)-1]))
    print("Line 4:")
    print("Busiest Station : %s (%d)"%(Line4_name[0],Line4[0]))
    print("Least used Station : %s (%d)"%(Line4_name[len(Line4)-1],Line4[len(Line4)-1]))


if __name__=="__main__":
    main()