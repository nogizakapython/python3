input_line = input()
array1 = list(map(int,input_line.split(' ')))
W = array1[0]
R = array1[1]
for i in range(R):
    for j in range(W):

        if j == W - 1:
            print(j+1)
        else:
            print(j+1,end=" ")
