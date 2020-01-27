from nornir import InitNornir
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import files, text
from nornir.core.inventory import ConnectionOptions

BACKUP_PATH = "/Users/fitzadd/Documents/NetDevOps/GitHub/nornir/output"

def backup_config(task, path):
    r = task.run(
        task=networking.netmiko_send_command,
        command_string="show running-config"
    )
    task.run(
        task=files.write_file,
        filename=f"{path}/{task.host}-running-config.txt",
        content=r.result
)

#Initialise Nornir
nr = InitNornir()
#Filter Nornir by specifying device type
devices = nr.filter(name="arista-1")

result = devices.run(
    name="Device Config Backup", path=BACKUP_PATH, task=backup_config
)
print_result(result)