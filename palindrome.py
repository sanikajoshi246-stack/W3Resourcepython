n = int(input())
temp=n
rev=0
while temp>0:
  last_digit=temp%10
  rev=(rev*10)+last_digit
  temp=temp//10
if(n==rev):
  print("Yes")
else:
  print("No")
