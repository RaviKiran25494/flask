# <!-- C:\\Users\\ravikiran\\Desktop\\flask8\\scrapyflask\\items1 -->
import csv
#path=open("C:\\Users\\LeburiL\\Desktop\\hello.csv", 'a')
# file=csv.writer(path,delimiter=' ')
# a=['harika,abc@gmail.com,A,P'.split(","),'Apparna,app@gmail.com,A,P'.split(","),'Hari,hari@gmail.com,A,P'.split(","),'chari,chr@gmail.com,A,A'.split(","),'5,5,3,2,4'.split(",")]
# for row in a:
#     file.writerow(row)

path1=open("C:\\Users\\ravikiran\\Desktop\\flask8\\scrapyflask\\items1.csv", 'r')
file=csv.reader(path1)
list1=[]
list2=[]
for row in file:
   list2.append(row)
   a=len(row)

   if(a>3):
       if(row[3]=='P'):
           list1.append(row)
           path2=open("C:\\Users\\LeburiL\\Desktop\\hai.csv", 'w')
           file2=csv.writer(path2)
           file2.writecolum(list1)
   else:
       continue
print(list1)