import subprocess
def ping_insecure(myserver):
  return subprocess.call(f'ping -c 1 {myserver}', shell=True)

print(ping_insecure('8.8.8.8 & touch file'))    # 

