Proof of concept for NX-OS CLI API. This was tested on a Cisco Nexus 9300v image running NX-OS version 10.5(1)
on the CML-2.8 platform.

Don't forget your target device requires: R1(config)# feature nxapi

Also, this API has its own GUI (in fact, two of 'em) as the above command starts an nginx instance. 
Go to https://{ip} for the NX-API Sandbox or https://{ip}/visore.html for the NX REST object model.