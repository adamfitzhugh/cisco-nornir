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


#    print(f"Pre/post checks from (task.host)")

    #Create for loop to loop over the commands
    for cmd in commands:
        #Run the command against the device and store it in out
        out = task.run(task=netmiko_send_command, command_string=cmd)
#        #Save the output
#        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#        task.host["info"]="\n"+2+"#"+40+"\n"+cmd" : "+ts+"\n"+"#"+40+"\n"+2+out.result 
#        task.host["info"]="\n"+2+"#"+40+"\n"+cmd+ts+"\n"+"#"+40+"\n"+2+out.result
#        #Create output files
#        task.run(task=files.write_file,filename=f"/Users/fitzadd/Documents/NetDevOps/GitHub/nornir/output/{task.host}_pre_change_checks.txt",content=task.host["info"],append=True)
        print(out)

def main():
    #Initialise Nornir
    n = InitNornir()
    #Filter Nornir by specifying device type
    n = n.filter(platform="arista_eos")
    #Run the check_commands function
    n.run(task=check_commands)
    print_result(task)

#    #Open the pre and post change text files and store them in a variable called diff
#    with open("/Users/fitzadd/Documents/NetDevOps/GitHub/nornir/output/{task.host}_pre_change_checks.txt") as pre_check_file, open("/Users/fitzadd/Documents/NetDevOps/GitHub/nornir//Users/fitzadd/Documents/NetDevOps/GitHub/nornir/output/{task.host}_post_change_checks.txt"):
#        diff = difflib.ndiff(pre_check_file.readlines(), post_check_file.readlines())
#    #Loop over the documents and store the changes in the below text file
#    with open ("post_change_diff.txt", "w") as result:
#        for output in diff:
#            result.write(output)

if __name__== "__main__":
    main()
