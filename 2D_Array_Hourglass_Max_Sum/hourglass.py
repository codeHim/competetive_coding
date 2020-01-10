
def validateMatrix(arr):
    flag = 0 
    if (len(arr) == 6):
        for i in arr:
            if (len(i) == 6):
                pass
            else:
                flag = 1
                break
    
    return flag

def hourglass(arr):
   validate = validateMatrix(arr)
   max_sum = 0
   rows = 6
   column = 6
   if validate == 0:
       for r in range(0,rows-2):
           for c in range(0,column-2):
               sum = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] +arr[r+2][c] + \
                    arr[r+2][c+1] + arr[r+2][c+2]
               max_sum = max(max_sum,sum)
       return max_sum
   else:
        print ('Invalid input!! Enter 6x6 matrix!!')
        return 0

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass(arr)
    print (result)