import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
env = Environment(loader=FileSystemLoader("."))

print("\n ********* Welcome Guys,Here You will see some configuration protocols on my eve virtual router ( automate this conf using jenkins) ******** \n")

protocol= input("Do you want bgp or ospf or static protocol ! : ")

if protocol == "bgp" :
    with open("bgp.yaml") as file1:
        data1 =yaml.load(file1, Loader=yaml.FullLoader)
    temp = env.get_template("bgp.j2")
    x = temp.render(a=data1)
    vxr = ConnectHandler(host="192.168.1.23", username="khamis", password="khamis", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(x)
    show = vxr.send_command_timing("do show bgp summary")
    print(show)
elif protocol == "ospf" :
    with open("ospf.yaml") as file2:
        data2 = yaml.load(file2, Loader=yaml.FullLoader)
    temp = env.get_template("ospf.j2")
    y = temp.render(a=data2)
    vxr = ConnectHandler(host="192.168.1.23", username="khamis", password="khamis", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(y)
    show = vxr.send_command_timing("do show run")
    print(show)
elif protocol == "static" :
    with open("static.yaml") as file3:
        data3 = yaml.load(file3, Loader=yaml.FullLoader)
    temp = env.get_template("static.j2")
    z = temp.render(a=data3)
    vxr = ConnectHandler(host="192.168.1.23", username="khamis", password="khamis", device_type="cisco_ios")
    vxr.enable()
    vxr.config_mode()
    vxr.send_command_timing(z)
    show = vxr.send_command_timing("do show run")
    print(show)
else:
    print(" please write only protocols :  bpg or ospf or staic only !!!")


