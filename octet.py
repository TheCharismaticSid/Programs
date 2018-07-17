import ipaddress
def makeaddr(a,b,c,d):
    return ipaddress.IPv4Address(bytes([a,b,c,d]))  #creating and address with these bytes

def ip():
    for x in range(256): 
        print(makeaddr(0, 0, 0, x))    #for 0.0.0.1 to 0.0.0.255
    for x in range(256):
        print(makeaddr(0, 0, x, 255)) #for 0.0.1.255 to 0.0.255.255
    for x in range(256):
        print(makeaddr(0, x, 255, 255)) #for 0.1.255.255 to 0.255.255.255
    for x in range(256):
        print(makeaddr(x, 255, 255, 255)) #for 1.255.255.255 to 255.255.255.255



for addr in ip():  #for prining out each for loop of def ip() function
    print(addr)
    

