#Names: Steven Condor | Devin Delgado
#Date: 2022.04.30
#Application: Distance Vector Routing Protocols
#Purpose:

import os
import sys
import socket
import threading
import time

error3 = "There was an error\n"

def options():
    print("Enter a command:\n")
    print("help\n")
    print("update <server-ID1> <server-ID2> <Link Cost>\n")
    print("step\n")
    print("packets\n")
    print("display\n")
    print("disable <server-ID>\n")
    print("crash\n")

def update(serverId1, serverId2, linkCost):
    print("Test Update: " + serverId1 + ", " + serverId2 + ", " + linkCost + "\n")
    return
    
def step():
    print("Test Step\n")
    return
    
def packets():
    print("Test Packets\n")
    return
    
def display():
    print("Test Display\n")
    return
    
def disable(serverId):
    print("Test Disable " + serverId + "\n")
    return
    
def crash():
    print("Test Crash\n")
    return
    
def runStart(topologyFileName, routingUpdateInterval):
    print("Test: "+topologyFileName+", "+routingUpdateInterval+"\n")
    return

def startUp():
    print("server -t <topology-file-name> -i <routing-update-interval>\n")
    command = input("Please enter command:\n")
    param = command.split()
    if(param[0] == "server" and param[1] == "-t" and param[3] == "-i"):
        runStart(param[2], param[4])
    else:
        print("Input Error\n")
        startUp()
        

if __name__ == "__main__":
    startUp()
    options()
    while True:
        command = input("Please enter command:\n")
        param = command.split()
        #implement a len(param) == 1 for all single param commands
        if len(param) == 0:
            print(error3)
        elif param[0] == "crash":
            if len(param) > 1:
                print(error3)
                continue
            print("Closing all connections...\n")
            break
        elif param[0] == "help":
            if len(param) > 1:
                print(error3)
                continue
            options()
        elif param[0] == "update":
            if len(param) > 4:
                print(error3)
                continue
            update(param[1], param[2], param[3])
        elif param[0] == "step":
            if len(param) > 1:
                print(error3)
                continue
            step()
        elif param[0] == "packets":
            if len(param) > 1:
                print(error3)
                continue
            packets()
        elif param[0] == "display":
            if len(param) > 1:
                print(error3)
                continue
            display()
        elif param[0] == "disable":
            if len(param) > 2:
                print(error3)
                continue
            disable(param[1])
        else:
            print(error3)
    time.sleep(3)
    os._exit(0)


