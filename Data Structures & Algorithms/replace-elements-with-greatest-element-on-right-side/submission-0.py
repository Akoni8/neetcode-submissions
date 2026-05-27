class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)

        for num1 in range(size):
            max_num = -1
            for num2 in range(num1+1, size):
                if arr[num2] > max_num:
                    max_num = arr[num2]
            arr[num1] = max_num
        
        arr[size -1] = -1
        return arr