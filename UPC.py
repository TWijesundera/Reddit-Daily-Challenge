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

    if len(upc_code) == 12:
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
                print "Final number is correct"
            else:
                print "Final number is incorrect"
        else:
            if (10-modulo_M) == check:
                print "True"
            else:
                print "False"
    elif len(upc_code) == 11:
        for number in upc_code:
            upc_list.append(number)

        for x in range(0, len(upc_list)):
            if x % 2 == 0:
                even_sum += int(upc_list[x])
            else:
                odd_sum += int(upc_list[x])

        even_sum = even_sum * 3
        modulo = odd_sum + even_sum
        if modulo % 10 == 0:
            print "The final number is %d" % ((modulo % 10))
        else:
            print "The final number is %d" % (10 - (modulo % 10))
    else:
        for number in upc_code:
            upc_list.append(number)

        length = len(upc_code)
        length = 11 - length

        append_list = [0] * length
        upc_list = append_list + upc_list


        for x in range(0, len(upc_list)):
            if x % 2 == 0:
                even_sum += int(upc_list[x])
            else:
                odd_sum += int(upc_list[x])

        even_sum = even_sum * 3
        modulo = (odd_sum) + even_sum
        if modulo % 10 == 0:
            print "The final number is %d" % ((modulo % 10))
        else:
            print "The final number is %d" % (10 - (modulo % 10))

upc("036000291452")
upc("03600029145")
upc("1234567")
