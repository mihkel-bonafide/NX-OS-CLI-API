import requests
import json
import urllib3

from show_version import get_version
urllib3.disable_warnings()
from lehost import host, username, pword

"""
Working code that demonstrates the functionality of NX-API CLI, here demonstrating the "show interface mac-address" command. This was tested 
on a Cisco Nexus 9300v image running NX-OS version 10.5(1) on the CML-2 platform.

"""

def get_macs():

  myheaders={'content-type':'application/json'}
  payload={
    "ins_api": {
      "version": "1.0",
      "type": "cli_show",
      "chunk": "0",
      "sid": "sid",
      "input": "show interface mac-address",
      "output_format": "json"
    }
  }

  response = requests.post(host,data=json.dumps(payload), headers=myheaders,auth=(username,pword), 
                         verify=False).json()["ins_api"]["outputs"]["output"]["body"]
  return response

def main():
    print(f"This is the raw output from running the 'show interface mac-address' command on a target Cisco Nexus 9300v device")
    command_output = get_macs()
    print(f"Command output:\n{json.dumps(command_output, indent=2)}")


if __name__ == "__main__":
    main()
