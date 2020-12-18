import requests 
 
start, end = 1, 100

sname = input("Enter A Url :")
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
#By HithMast
