### Lists ###

my_list = list();
my_other_list = [];

print(len(my_list))

my_list = [35,24,62,52,30,30,17]
print(type(my_list))

my_other_list = [35,1.77, "Brairs","Moure"]
print(type(my_other_list))

## Arreglo Bidimensional

def hourglassSum(arr):
    # Write your code here
  maxSum = -99
  
  for i in range(4):
     for j in range(4):
        top = sum(arr[i][j:j+3])
        mid = arr[i + 1][j + 1]
        bot = sum(arr[i + 2][j:j+3])
        
        hourGlass = top + mid + bot
        maxSum = max(hourGlass,maxSum) 
        
         
  return maxSum


