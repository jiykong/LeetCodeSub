Problem was the first problem I solved in a while and I realized how rusty I was.

Initially I assumed we can simply do a merge sort but I realized that the problem are tne no return + modify nums1 in-place rule.

So I opted to initially splice the array together and do self = self.sort().

Although this solution works, I felt that this solution is not the type of solution that would fly since I used a in library method.

So I opted to do a deeper dive by editing the array by post splicing and doing a bubble sort. I'm persoanlly not a fan of bubble sort however but couldn't think of anything outside bubble / merge sort, so I then opted to look at solutions.

Best Python Solution, Faster Than 99%, One Loop, No Splicing, No Special Case Loop by sharifzad
His solution was what made most logical sense to me as it is easy to read and takes advantage of the 0s in the nums1 array.

I took a quick glance at it and was able to replicate it.
