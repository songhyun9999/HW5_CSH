import csv
def main():
    f = open('q1.csv',encoding='cp949')
    data = csv.reader(f)
    header = next(data)
    max = 0
    min = 0
    avg_temp = 0
    
    total = 0
    for row in data:
        if(row[2]!=''and row[3]!=''and row[4]!=''):
            row[2]=float(row[2])
            row[3]=float(row[3])
            row[4]=float(row[4])
            avg_temp = avg_temp + row[2]
            max = max + row[4]
            min = min + row[3]
            total=total+1

    avg_temp=avg_temp/total
    max = max / total
    min = min/total
    print("***Annual Temperature Report for Seoul in 2022***")
    print("Average Temperature : %.2f Celsius"%(round(avg_temp,2)))
    print("Average Minimum Temperature : %.2f Celsius"%(round(min,2)))
    print("Average Maximum Temperature : %.2f Celsius"%(round(max,2)))   
    f.close()

if __name__=="__main__":
    main()