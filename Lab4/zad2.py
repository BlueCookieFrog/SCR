import time
import signal
import sys


def terminateProcess(signalNumber, frame):
    print(f"Recived: {signalNumber} terminating the process")
    sys.exit()

def reciveSignal(signalNumber, frame):
    print(f"Recived: {signalNumber}")
    return

def sigPass(signalNumber, frame):
    pass

def sigDefine():
    signal.signal(signal.SIGTERM, terminateProcess)
    signal.signal(signal.SIGALRM, reciveSignal)
    signal.signal(signal.SIGUSR1, reciveSignal)
    signal.signal(signal.SIGUSR2, reciveSignal)

def sigDefinePass():
    #nie ignoruję SIGTERM by uniknąć problemów z terminacja programu
    signal.signal(signal.SIGALRM, sigPass)
    signal.signal(signal.SIGUSR1, sigPass)
    signal.signal(signal.SIGUSR2, sigPass)

if __name__ == '__main__':

    sigDefine()

    i = 0
    while True:
        if ((i//5)%2):
            sigDefinePass()
            print("Ignoring signals")
        else:
            sigDefine()
            print("Handling signals")
        i = i + 1
        time.sleep(1)
