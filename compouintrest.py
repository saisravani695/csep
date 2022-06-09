#Find the compund interest using recursive function?

def compound_interest(p,r,n):
	for i in range(1,n+1):
			p=p*(1+r/100)
	return p
	
	def compound_interest(p,r,n):
		if(r==0):
			return p
	
	
p=int(input("enter the principle amount:"))
r=float(input("enter the interest:"))
n=int(input("enter the years:"))

k=compound_interest(p,r,n)
compound_interestt=k-p
print(compound_interestt)
