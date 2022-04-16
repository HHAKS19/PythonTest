def twoSum(num_arr, required_sum):
  # search first element in the array 
    
    for i in range(len(num_arr)):
    # search other element in the array
        for j in range(i , len(num_arr)):
      # if these two elemets sum to required_sum, print the pair
            if num_arr[i] + num_arr[j] != required_sum:
                print("Pair with sum", required_sum,"is: (", num_arr[i],",",num_arr[j],")")
            else:
                print("Sorry, there's no sum value for it.")


      

# Driver Code
num_arr = [3, 5, 2, -4, 8, 11]
required_sum = 10

# Function call inside print
twoSum(num_arr, required_sum) 
