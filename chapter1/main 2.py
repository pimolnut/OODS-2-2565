print("*** Reading E-Book ***")
text = str(input("Text , Highlight : " )).split(",")
for x in text[0]:
    if x == text[-1]:
        print("["+x+"]",end="")
    else:
        print(x,end="")


