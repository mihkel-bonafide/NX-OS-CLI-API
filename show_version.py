import requests
import json
import urllib3
urllib3.disable_warnings()
from lehost import host, username, pword

"""
Working code that demonstrates the functionality of NX-API CLI, here demonstrating the "show version" command. This was tested 
on a Cisco Nexus 9300v image running NX-OS version 10.5(1) on the CML-2 platform.

"""

def get_version():
  myheaders={'content-type':'application/json'}
  payload={
    "ins_api": {
      "version": "1.0",
      "type": "cli_show",
      "chunk": "0",
      "sid": "sid",
      "input": "show version",
      "output_format": "json"
    }
  }

  response = requests.post(host,data=json.dumps(payload), headers=myheaders,auth=(username,pword), 
                         verify=False).json()["ins_api"]["outputs"]["output"]["body"]
  return response

def main():
  print(f"This is us running the 'get version'command on a Cisco Nexus 9300v")
  command_output = get_version()
  version = command_output["nxos_ver_str"]
  file_name = command_output["nxos_file_name"]
  chassis_id = command_output["chassis_id"]
  cpu_name = command_output["cpu_name"]
  memory = command_output["memory"]
  
  print()
  print(f"Software version: {version}")
  print(f"File name: {file_name}")
  print(f"Chassis ID: {chassis_id}")
  print(f"CPU type: {cpu_name}")
  print(f"Memory: {memory}")

if __name__ == "__main__":
  main()
