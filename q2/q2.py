import csv
def main():
    f = open('q2.csv',encoding='cp949')
    data = csv.reader(f)
    header = next(data)
    max=-999999
    min = 999999
    Ldate=""
    Sdate=""
    diff = 0
    for row in data:
        if(row[2]!=''and row[3]!=''and row[4]!=''):
            row[3]=float(row[3])
            row[4]=float(row[4])
            diff = row[4]-row[3]
            if(diff>max):
                max=diff
                Ldate=row[0]
            if(diff<min):
                min=diff
                Sdate=row[0]
    print("***Annual Temperature Report for Seoul in 2022***")
    print("Day with the Largest Temperature Variation : %s"%(Ldate))
    print("Maximum Temperature Difference : %.1f Celsius"%(round(max,1)))
    print("Day with the Smallest Temperature Variation : %s "%(Sdate))
    print("Minimum Temperature Difference : %.1f Celsius"%(round(min,1)))
    f.close()

if __name__=="__main__":
    main()