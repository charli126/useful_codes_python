def computepay(h,r):
    if h <= 40:
        return h*r
    else: 
        return 40*r+(h-40)*r*1.5
    
hrs = input("Enter Hours:")
try:
    h = float(hrs)
except: 
    h = -1
if h < 0:
    print ("Error, please enter a numeric value")
else:
    rate = input ("Enter Rate:")
    try: 
        r = float(rate)
    except: 
        r = -1
    if r < 0:
        print ("Error, please enter a numeric value")
    else:
        p = computepay(h, r)
        print ("Pay", p)
