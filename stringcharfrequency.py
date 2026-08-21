str=input("Enter a string:")
frequency={}
for chr in str:
   if chr in frequency:
      frequency[chr] += 1
   else:
      frequency[chr] = 1

print(frequency)    
