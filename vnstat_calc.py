from decimal import Decimal

#testVar = raw_input("The name of the log file? ")
#f=open(testVar,'r')

import subprocess
subprocess.call("vnstat -u && vnstat -d > log.txt", shell=True)

f=open("log.txt","r")

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

signcounter=0
total=0
calc_counter=0
print "This program will calculate the total traffic transferred \n(without including today's inaccurate and superstitious estimates.) \n"

for line in f:
    newlist=[]
    locations=findOccurences(line, "|")
    seperator=findOccurences(line,"-")
    if seperator != []:
        signcounter=signcounter+1
#    print seperator,signcounter
    if len(locations)>0:
        thevalue=line[(locations[1]+1):(locations[1]+9)]
    	theunit=line[(locations[1]+10)]
#        if "t" not in thevalue and signcounter!=2:
        if "t" not in thevalue and signcounter!=2 and calc_counter<30:
            calc_counter=calc_counter+1
#            print thevalue
            result=Decimal(thevalue)
            if theunit=="G":
                total=total+result
            else:
                total=total+result/1024
#            print total

print "Total:",total,"GiB"
print "Total:", (total*1024),"MiB"
subprocess.call("rm log.txt", shell=True)
