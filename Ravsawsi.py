# import math
# pi = int(str(math.pi).replace(".",""))
pi="3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679".replace(" ","").replace(".","")
# Taking input plaintext
pt = input("Enter text to be encrypted\n").upper()
et=[]
for i in range(len(pt)):
    x = ord(pt[i]) + int(pi[i])
    if x > ord('Z'):
        x=x-26;    
    et.append(chr(x))
et = "".join(et)
print("The Encrypted text is:\n" + et)
