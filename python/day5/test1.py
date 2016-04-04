n = int(input())
a = []
for i in range(n):
 row = input().split()
 for i in range (len(row)):
  row[i] = int (row[i])
 a.append(row)
print(a) 
