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
	        if(array[k-low] - x) <  (array[k+high] - x):
		        closest.append(array[k-low])
		        low +=1
	        elif (array[k+high] - x) < (array[k-low] - x):
		        closest.append(array[k + high])
		        high +=1
	        elif (array[k + high] - x) == (array[k-low] - x):
		        closest.append(array[k - low])
                low +=1  
        closest.sort()
        return closest

                       
    def binarysearch(self,arr,x,begindex, endindex):
	mid = (begindex + endindex)/2
    if x == arr[mid] or array[mid] - x < array[mid+1] - x or array[mid] - x < array[mid-1] - x:
            return index
    elif x > arr[mid]:
	        binarysearch(x, mid, endindex)
    elif x < arr[mid]:
	        binarysearch(x, beginindex,mid)

            
        