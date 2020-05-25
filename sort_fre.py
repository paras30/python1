s=input("sort\nenter a string : ")
dict={}
result=' '
for i in s:
	if i in dict:
		dict[i]+=1
	else:
		dict[i]=1
s=sorted(dict,key=lambda x:dict[x],reverse=True)
for i in s:
	result+=i*dict[i]
print(f"Sort Characters By Frequency is:{result}")
			
        