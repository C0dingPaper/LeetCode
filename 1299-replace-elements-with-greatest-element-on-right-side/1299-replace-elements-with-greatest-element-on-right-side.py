class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # i start at the first indice of the array say 0
        # For this i need to find the max value of the REST of the array wout indice 0
        # Do this until the end and once i reach the len(arr) index replace it with -1
        # Dont replace the last index with -1 because you might need to update other elements
        # THE SOLUTION BELOW WORKS BUT EXCEEDS TIME LIMIT FOR BIG INPUTS THO IT HAS O(N^2) COMPLEXITY
        # i = 0
        # if len(arr) == 1:
        #     arr[0] = -1
        #     return arr
                
        # for i in range(len(arr)-1):
        #     remove_first_element = arr[i+1:]
        #     max_value = max(remove_first_element)
        #     if len(arr) - i > 1:
        #         arr[i] = max_value
        #     else:
        #         arr[i] = arr[i+1]
        #         break
                
        # # arr = [17,18,5,4,6,1]
        # arr[-1] = -1
        # return arr
        # ------------------------------------------------------------------------------------
        max_so_far = -1                
        for i in range(len(arr) - 1, -1, -1):   # i goes: last, ..., 0
            current = arr[i]            # save original value
            arr[i] = max_so_far         # replace with max to the right
            max_so_far = max(max_so_far, current)  # update max_so_far using original value
        return arr