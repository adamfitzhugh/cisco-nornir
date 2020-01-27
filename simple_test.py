from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.files import write_file

nr = InitNornir()

result = nr.run(
    task=netmiko_send_command,
    command_string="show ip int bri"
)
result_1 = nr.run(
    task=netmiko_send_command,
    command_string="show running-config"
)
print_result(result)
print_result(result_1)
