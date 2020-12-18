import requests 
 
start, end = 1, 81

#event_lis = range(start, end + 1)[start%1::2]
#for num in event_lis:
  #  print(num, end= " ")

sname = input("Enter A Url : ")
lst = list()
for num in range(start, end + 1 ):
    if num % 2 != 0:
        lst.append(num)

for num in lst:
    r = requests.get(sname+'/'+str(num))
    r.headers['content-type']
    print(r.url)
    print(r.json())
    print(r.status_code)
