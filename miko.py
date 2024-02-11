import netmiko
import re


class Device:

    def __init__(self, ip, username, password, device_type):
        self.ip = ip
        self.username = username
        self.password = password
        self.device_type = device_type

    def connect(self):
        return netmiko.ConnectHandler(ip=self.ip, username=self.username, password=self.password, device_type=self.device_type)

    def send_command(self, command):
        return self.connect().send_command(command)

    def send_config_set(self, config):
        return self.connect().send_config_set(config)

    def send_show_ip_int_brief(self):
        shipintbrief_pattern = r'(\S+)\s+(\S+)\s+\S+\s+\S+\s+(\S+)\s+(\S+)'
        matches = re.findall(shipintbrief_pattern, self.connect().send_command("show ip int brief"))
        for match in matches:
            print("Interface:", match[0])
            print("IP Address:", match[1])
            print("Status:", match[2])
            print("Protocol:", match[3])
            print()
        self.connect().disconnect()

    def send_show_run(self):
        shrun_pattern = r'(\S+)\s+(.+?)\s*!?\n'
        matches = re.findall(shrun_pattern, self.connect().send_command("show run"))
        for match in matches:
            print("Section:", match[0])
            print("Content:")
            print(match[1])
            print()
        self.connect().disconnect()

    def disconnect(self):
        return self.connect().disconnect()

if __name__ == '__main__':
    device = Device(ip='192.168.5.21', username='admin', password='cisco', device_type='cisco_ios')
    device2 = Device(ip='192.168.5.22', username='admin', password='cisco', device_type='cisco_ios')
    device3 = Device(ip='192.168.5.23', username='admin', password='cisco', device_type='cisco_ios')

    device.send_show_ip_int_brief()
    device.send_show_run()