    def searchRange(self, nums, target):
        n = len(nums)
        if n==0:
            return [-1,-1]      
        def lower_bound(x):
            left,right = 0,n-1
            while left<=right:
                mid = left+(right-left)//2
                if nums[mid]>=x:
                    right = mid-1
                else:
                    left = mid+1
            return left
        L = lower_bound(target)
        if  L==n or nums[L]!=target:
            return [-1,-1]        
        R = lower_bound(target+1)-1
        return[L,R]