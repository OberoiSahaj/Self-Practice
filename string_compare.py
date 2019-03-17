import difflib

main_domain= input("Enter single domain : ")
n= int(input("Enter number of domains in list: "))

l=[] #Creating empty list

for i in range(1, n+1):
    x= input("Enter domain " + str(i) + ":  ")  # Loop to enter the domains in a list
    l.append(x)

for test_domain in l:
    seq = difflib.SequenceMatcher(isjunk=None,a=main_domain,b=test_domain).ratio()  # This statement checks our main/single domain with the domains in the list
    per= round(seq*100, 2)   #Rounding off the percentage match upto 2 decimal
    print("Percent match for " + test_domain + " is "+str(per))