message = input("Write your text here: ")
f = open("usermsg.txt","w")
f.write(message)
f.close

'''f = open("usermsg.txt","r")
print(f.read())'''