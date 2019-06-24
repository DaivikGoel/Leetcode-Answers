class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        index = self.binarysearch(arr,x, 0, len(arr) - 1)
        closest = []
        if k % 2 == 1:
            low = 0
            high = 0
        while low + high != k:
	        if(arr[k-low] - x) <  (arr[k+high] - x):
		        closest.append(arr[k-low])
		        low +=1
	        elif (arr[k+high] - x) < (arr[k-low] - x):
		        closest.append(arr[k + high])
		        high +=1
	        elif (arr[k + high] - x) == (arr[k-low] - x):
		        closest.append(arr[k - low])
                low +=1  
        closest.sort()
        return closest

                       
    def binarysearch(self,arr,x,begindex, endindex):
        mid = (begindex + endindex)/2
        if x == arr[mid] or arr[mid] - x < arr[mid+1] - x or arr[mid] - x < arr[mid-1] - x:
                return index
        elif x > arr[mid]:
                binarysearch(x, mid, endindex)
        elif x < arr[mid]:
                binarysearch(x, beginindex,mid)

            
        