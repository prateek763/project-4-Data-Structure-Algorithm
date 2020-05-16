def sqrt(number):
         if number<0:
                  return None
         elif number==0 or number==1:
                  return number
         else:
                  begin=0
                  last=number//2
                  while begin<=last:
                           mid=(begin+last)//2
                           sq=mid*mid
                           if sq==number:
                                    return mid
                           elif sq<number:
                                    begin=mid+1
                                    output=mid
                           else:
                                    last=mid-1
                  return output
         

print ("Pass" if  (3 == sqrt(9)) else "Fail")
# Output:-Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# Output:-Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# Output:-Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# Output:-Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# Output:-Pass

print(sqrt(-1))
# Output:-None
print(sqrt(9876543210))
# Output:-99380
