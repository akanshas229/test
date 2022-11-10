n1 = int(input("Enter no. of input"))
output = 0
sample_output = 0
for j in range(n1):
    x, y = map(int,input().split())
    x = int(str(int(str(x)[::-1])))
    y = int(str(int(str(y)[::-1])))
    output = int(x)+int(y)
    sample_output = int(str(output)[::-1])
    print(sample_output)
