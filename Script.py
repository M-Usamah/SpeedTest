from timeit import main
import speedtest

speed_test = speedtest.Speedtest()

def Download():
    speed = int(speed_test.download()/1024/1024)
    return speed
def Up():
    return speed_test.upload()/1024/1024

if __name__ == "__main__":
    print(Download())