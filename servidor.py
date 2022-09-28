import socket
from unittest import result
import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

Ox = screenWidth/2
Oy = screenHeight/2
pyautogui.moveTo(Ox, Oy)
x = 0
i=0
valorx = 0 
valory = 0 
Px = Ox
Py = Oy
aux=0

HOST = '192.168.1.65'
PORT = 123            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, client = tcp.accept()
    #print( 'Client: ', client)
    while True:
        msg = con.recv(6)
        if not msg: break
        #print( client, msg)
        #print(int(msg[i]),end='')
        
        valorx = msg.decode()#RECEBENDO DADOS DO ESP
        aux = aux + 1
        #result= ''.join(msg)

    #Correção das posições negativas
    valorx = int(valorx)
    if aux == 2:
        valorx = valorx * -1
    elif aux == 1:
        valorx = abs(valorx)
    print(valorx)
    aux=0

    #valorx = x
    #valory = y

    # #Tratamento para limite de bordas
    #if  valorx == Px:
    #     px = 0
    #elif valory == y:
    #     y=0
    #if Px <= 0:
    #     px = 0
    #elif Px >= screenWidth:
    #elif Py < 0:
    #     Py = 0
    #elif Py > screenHeight:
    #     Py = screenHeight

    if (valorx < -5):   #X DIREITA
         #abs(valory)
         Px = Px - valorx
         #Py = Py - valory
         #pyautogui.moveTo(Px, Oy-1)
         pyautogui.moveTo(Px, Py, duration=0.1, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
    elif (valorx > 5): #X ESQUERDA 
         #abs(valory)
         Px = Px - valorx
         #Py = Py + valory
         pyautogui.moveTo(Px, Py, duration=0.1, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

        

        # valorx = x
        # valory = y

    #print(" ")
    print( 'Closing connection to: ', client)
    con.close()

