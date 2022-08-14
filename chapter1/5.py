num = input("Enter All Bid : ").split()
if len(num) <= 1:
    print("not enough bidder")
else:
    num_to_int = []
    for item in num:
        num_to_int.append(int(item))
    num_to_int.sort()
    if num_to_int[-1] == num_to_int[-2]:
        print("error : have more than one highest bid")
    else:
        print(f"winner bid is {num_to_int[-1]} need to pay {num_to_int[-2]}")


