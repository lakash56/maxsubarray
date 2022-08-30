def max_corssing_subarray(mylist,low,mid,high):
    left_sum =float('-inf')
    sum = 0
    for i in range(mid-1,low-1,-1):
        sum=sum + mylist[i]
        if sum> left_sum:
            left_sum=sum
            max_left =i
    right_sum=float('-inf')
    sum=0
    for j in range(mid,high):
        sum=sum+mylist[j]
        if sum>right_sum:
            right_sum=sum
            max_right =j
    return(max_left,max_right,left_sum+right_sum)

    
def maxsubarray (mylist,low, high):
    if high==low:
        return(low,high,mylist[low])
    else:
        mid = (low+high)//2 #finds the mid point of the array
        left_low,left_high,left_sum =maxsubarray(mylist,low,mid)
        right_low,right_high,right_sum=maxsubarray(mylist,mid+1,high)
        cross_low,cross_high,cross_sum =max_corssing_subarray(mylist,low,mid,high)
        if(left_sum>=right_sum and left_sum>=cross_sum):
            return(left_low,left_high,left_sum)
        elif(right_sum>=left_sum and right_sum>=cross_sum):
            return(right_low,right_high,right_sum)
        else:return(cross_low,cross_high,cross_sum)




mylist =[34,-33,16,-1,-53,12,44,-56,67]

print('Max sum of sub array: ')