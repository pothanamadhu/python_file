import csv
import matplotlib.pyplot as plt
b=[]
d={}
with open("real_data.csv")as f1:
      data=list(csv.reader(f1))
      for i in data[1:]:
            if i[6]=="Evening":
                  b.append(i)
      for i in b:
            if i[2] not in d.keys():
                  d[i[2]]=1
            else:
                   d[i[2]]+=1
      print(d)
plt.bar(d.keys(),d.values())
plt.show()

                  
            
