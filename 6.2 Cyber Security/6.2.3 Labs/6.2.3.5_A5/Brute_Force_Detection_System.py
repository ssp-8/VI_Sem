from time import sleep
import threading
username = "admin"
password = "securepass"

login_attempts_failed = {}
blocked_ips = []

def block_ip(ip:str):
    sleep(30)
    print(f"IP {ip} can is unblocked")
    login_attempts_failed[IP] = 0
    blocked_ips.remove(ip)

if __name__ == "__main__":
    try:
        while True:
            IP = input("Enter your IP address (or type 'exit' to stop): ")
            if IP == 'exit':
                break

            if IP in blocked_ips:
                print(f"IP {IP} is blocked currently")
                continue

            user = input("Enter username: ")
            password_by_user = input("Enter password: ")
            if user == username and password_by_user == password:
                print(f"Login Successful for IP {IP}!")
            else:
                if login_attempts_failed.get(IP,None) == None:
                    login_attempts_failed[IP] = 1
                else:
                    login_attempts_failed[IP]+=1
                    if login_attempts_failed[IP] == 5:
                        print(f"Invalid 5 attempts. Wait for 30 seconds")
                        blocked_ips.append(IP)
                        t = threading.Thread(target=block_ip,args=(IP,),daemon=True)
                        t.start()

                if login_attempts_failed[IP] != 0 and IP not in blocked_ips:
                    print(f"Invalid credentials. Attemps left: {5-login_attempts_failed[IP]}")

    except KeyboardInterrupt:
        print("System Stopped by Force")