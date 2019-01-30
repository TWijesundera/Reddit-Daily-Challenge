"""
Generate sanity check for UPC codes
Steps:
    1) Sum the digits at odd-numbered positions (1st, 3rd, 5th, ..., 11th). If you use 0-based indexing, this is the even-numbered positions (0th, 2nd, 4th, ... 10th).

    2) Multiply the result from step 1 by 3.

    3) Take the sum of digits at even-numbered positions (2nd, 4th, 6th, ..., 10th) in the original number, and add this sum to the result from step 2.

    4) Find the result from step 3 modulo 10 (i.e. the remainder, when divided by 10) and call it M.

    5) If M is 0, then the check digit is 0; otherwise the check digit is 10 - M.
"""

def upc(upc_code):
    upc_list = []
    check = 0
    even_sum = 0
    odd_sum = 0

    for number in upc_code:
        upc_list.append(number)

    for x in range(0, len(upc_list)):
        if x == len(upc_list)-1:
            check = int(upc_list[x])
        if x % 2 == 0:
            even_sum += int(upc_list[x])
        else:
            odd_sum += int(upc_list[x])

    even_sum = even_sum * 3
    modulo = (odd_sum - check) + even_sum
    modulo_M = modulo % 10
    if modulo_M == 0:
        if modulo_M == check:
            print "True"
        else:
            print "Check Failed"
    else:
        if (10-modulo_M) == check:
            print "True"
        else:
            print "False"


upc("036000291452")