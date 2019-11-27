#Perform pre-change and post-change checks

from datetime import datetime
from nornir import InitNornir
from nornir.core.filter import F 
from nornir.plugins.tasks import text, files
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

def check_commands(task):
    
    #Run the following check commands
    commands = [
        "term len 0"
        "show version"
        "show running-config"
        "show log"
        "show interface status"
        "show interface description"
        "show interface trunk"
        "show port-channel summary "
        "show vlan"
        "show spanning-tree topology status"
        "show ip bgp summary"
        "show ip route summary"
        "show ip route"
    ]

    print(f"Pre/post checks from (task.host)")

    #Create for loop to loop over the commands
    for cmd in commands:
        #Run the command against the device and store it in out
        out = task.run(task=netmiko_send_command, command_string=cmd)
        #Save the output
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task.host["info"]="\n"+2+"#"+40+"\n"+cmd" : "+ts+"\n"+"#"+40+"\n"+2+out.result 

        #Create output files
        task.run(task=files.write_file,filename=f"output/{task.host}_change_checks.txt",content=task.host["info"],append=True)

def main():
    #Initialise Nornir
    n = InitNornir()
    #Filter Nornir by specifying device type
    n = n.filter(platform="arista_eos")
    #Run the check_commands function
    n.run(task=check_commands)

if __name__== "__main__":
    main()
