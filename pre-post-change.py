#Perform pre-change and post-change checks

import difflib

from datetime import datetime
from nornir import InitNornir
from nornir.core.filter import F 
from nornir.plugins.tasks import text, files
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

def check_commands(task):
    
    #Run the following check commands
    commands = [
        "show version",
        "show running-config",
        "show log",
        "show interface status",
        "show interface description",
        "show interface trunk",
        "show port-channel summary",
        "show vlan",
        "show spanning-tree topology status",
        "show ip bgp summary",
        "show ip route summary",
        "show ip route",
    ]

    print(f"Pre/post checks from {task.host}")

    #Loop over the above commands
    for cmd in commands:
        #Send the commands to the device and return to out
        out = task.run(task=netmiko_send_command, command_string=cmd)
        #Save the output with the current date and time
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task.host["info"]="\n"*4+"#"*80+"\n"+cmd+" : "+ts+"\n"+"#"*80+"\n"*4+out.result
        #Create the text file
        task.run(
            task=files.write_file,
            filename=f"{task.host}_device_checks.txt",
            content=task.host["info"],
            append=True
        )

def main():
    #Initialise Nornir
    n = InitNornir()
    #Filter Nornir by specifying device type
    n = n.filter(platform="arista_eos")
    #Run the check_commands function
    res = n.run(task=check_commands)
    print_result(res)

if __name__== "__main__":
    main()
