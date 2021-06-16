
from pythonping import ping 
import datetime
import os

def ping_device():

    currentdate = str(datetime.datetime.now())
    currentdate = currentdate.split('.')
    cdate = currentdate[0].split()
    rfilenm = ".".join(cdate)

    

    ip_list = ['8.8.8.8', '8.8.4.4', '192.168.32.54']

    for i in ip_list:
        #print("Pinging " + i + ":")
        response = ping(i, size=56, count=2)
        mini = response.rtt_min_ms
        maxi = response.rtt_max_ms
        avg = response.rtt_avg_ms
        print(f"Date: {rfilenm}, Website: {i}, rtt_min_ms: {mini}, rtt_max_ms: {maxi}, rtt_avg_ms: {avg}")


#################### OR ############################

    os_type = os.name
    #print(os_type)

    count = '-n' if os_type == 'nt' else '-c'

    for ip in ip_list:

        panswer  = os.popen(f"ping {ip} {count} 2").read()
        p = panswer.split("\n")

        if "Received = 5" and "Approximate" in panswer:
            print(f"UP {ip} Ping Successful")
        else:
            print(f"Down or Packet loss {ip} Ping Unsuccessful")
            print(f"Packet Loss: {p[len(p)-2].strip()}")



if __name__ == '__main__':
    ping_device()
