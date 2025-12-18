class Solution:
    def sortIt(self, arr):
        odd = []
        even = []
        
        for num in arr:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)
        
        odd.sort(reverse=True)
        even.sort()
        
        idx = 0
        for num in odd:
            arr[idx] = num
            idx += 1
        
        for num in even:
            arr[idx] = num
            idx += 1
