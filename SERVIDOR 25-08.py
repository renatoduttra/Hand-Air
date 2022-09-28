from pprint import pprint
import socket
from unittest import result
import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

Ox = screenWidth/2
Oy = screenHeight/2
pyautogui.moveTo(Ox, Oy)
x = 0
y=0
z=0
i = 0
valorx = 0 
valory = 0 
Px = Ox
Py = Oy
Pz = 0
aux = 0
vetorx = []
vetory = []
vetorc = []
vetor = []

HOST = '192.168.1.65'
PORT = 123            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, client = tcp.accept()
    print( 'Client: ', client)
    while True:
        msg = con.recv(1024)
        if not msg: break
        #print( client, msg)
        #print(int(msg[i]),end='')
        #for i in range(len(msg)):
            #vetorx.append(chr(msg[i]))
        vetorx.append(msg.decode())

            #c = chr(msg[i])
            #v = ""+c
            #vetorx=chr(msg[i])#RECEBENDO DADOS DO ESP
            #aux = aux + 1
            #result= ''.join(msg)
            #print(vetorx)
        vetor = "".join(vetorx)
        #vetorc = vetor.split()
        #with open("C:\\Users\\Ryzen\\Desktop\\maoesp\\esp+socket\\giro.txt", "w+") as arquivo:
        #   arquivo.write(str(vetor))
        #with open("C:\\Users\\Ryzen\\Desktop\\maoesp\\esp+socket\\giro.txt", "r") as arquivo:
        #    ot = arquivo.read()
        vetorx = vetor.split()
        for i in range(len(vetorx)):
            if i == 0:
                x = int(vetorx[0])
                #x = int(x)
                print(x)
            elif i == 1:
                y= int(vetorx[1])
                #y = int(y)
                print(y)
            elif i == 2:
                z= int(vetorx[2])
                #z = int(z)
                print(z)
        #x = vetorc[0]
        #print("X= ", vetorx)
        vetorx.clear()
    #i=0

    #Tratamento para limite de bordas
    if Px > screenWidth:
        Px = screenWidth
    elif Py < 0:
        Py = 0
    elif Py > screenHeight:
        Py = screenHeight

    Px = Px-(z * 2)
    Pz = Pz+(y * 1.4)
    
    pyautogui.moveTo(Px, Pz, duration=0.1, tween=pyautogui.easeInOutQuad) 
    Px, Pz = pyautogui.position()
    print( 'Closing connection to: ', client)
    con.close()