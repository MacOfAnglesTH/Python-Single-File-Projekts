######################################################################################################
# This Python generate the remmina profiles, for new installation slax servers.
# @author Mac Müller
# Date: 12.Aug.2025
######################################################################################################
######################################################################################################
######################################################################################################

import subprocess

TVS = "tvs"
filePath = "/root/.local/share/remmina/group_vnc_tvsName_tvsIp-5901.remmina"
PORT = ":5901"
labTVSip = { #configuration for each profile
		"GprivateLAB": {
		"ip": "private.168.3.private",
		"route_default": "private.168.3.1",
		"tvs": {
			"xLab_private_TVS1": "private.16.3.private1",
			"xLab_private_TVS2": "private.16.3.private2",
			"xLab_private_TVS3": "private.16.3.private3"
		}
		},    
		"CprivateLAB": {
			"ip": "private.168.3.31",
			"route_default": "private.168.3.1",
			"tvs": {
				"xLab_private_TVS1": "private.16.3.private1",
				"xLab_private_TVS2": "private.16.3.private2",
				"xLab_private_TVS3": "private.16.3.private3"
			}
		},
		"privateECTS": {
			"ip": "private.220.61.private",
			"route_default": "private.220.61.private",
			"tvs": {
				"privateECTS_227": "private.220.61.private1",
				"privateECTS_228": "private.220.61.private2"
			}
		},
		"privateFRO": {
			"ip": "private.16.3.private",
			"route_default": "private.16.3.1",
			"tvs": {
				"private137 (EPS FRO)": "private.16.3.private"
			},
			"tvs_rdp":{
				"private147 (WR2 FRO)": "private.16.3.private"
			}
		},
		"privateFRW": {
			"ip": "private.16.3.private",
			"route_default": "172.16.3.1",
			"tvs": {
				"private138 (EPS FRW)": "private.16.3.private"
			},
			"tvs_rdp":{
				"private148 (WR2 FRW)": "private.16.3.private"
			}
		},
		"privateVI": {
			"ip": "private.16.3.private",
			"route_default": "private.16.3.1",
			"tvs": {
				"private139 (EPS FRW)": "private.16.3.private"
			},
			"tvs_rdp":{
				"private (WR2 FRW)": "private.16.3.private"
			}
		},
		"privateVLBS": {
			"ip": "private.16.3.private",
			"route_default": "private.16.3.1",
			"tvs": {
				"FLAZ_LBS_TVS_01": "private.16.3.156",
                "FLAZ_LBS_TVS_02": "private.16.3.157",
                "FLAZ_LBS_TVS_03": "private.16.3.158"
			}
		},
		"privateZEVO1": {
			"ip": "private.220.61.private",
			"route_default": "private.220.61.1",
			"tvs": {
				"private201": "private.220.61.201",
				"private203": "private.220.61.203",
				"private249": "private.220.61.249",
				"private250": "private.220.61.250",
				"private251": "private.220.61.251",
				"private252": "private.220.61.252",
				"private253": "private.220.61.253",
				"private254": "private.220.61.254",
				"Nachbarstellwerke private211": "private.220.61.211"
			},
			"tvs_rdp":{
				"private241 (WR2 privateZEVO1)": "private.220.61.241",
				"private243 (WR2 privateZEVO1)": "private.220.61.243"
			}
		},
		"privateZEVO2": {
			"ip": "private.220.61.232",
			"route_default": "private.220.61.1",
			"tvs": {
				"EPS privateZEVO01 private201": "private.220.61.201",
				"EPS privateZEVO02 private202": "private.220.61.202",
				"EPS privateZEVO03 private203": "private.220.61.203",
				"EPS privateZEVO04 private204": "private.220.61.204",
				"EPS privateZEVO05 private205": "private.220.61.205",
				"EPS privateZEVO06 private206": "private.220.61.206",
				"private249": "private.220.61.249",
				"private250": "private.220.61.250",
				"private251": "private.220.61.251",
				"private252": "private.220.61.252",
				"private253": "private.220.61.253",
				"private254": "private.220.61.254",
				"Nachbarstellwerke private211": "private.220.61.211"
			},
			"tvs_rdp":{
				"private241 (WR2 privateZEVO1)": "private.220.61.241",
				"private242 (WR2 privateZEVO2)": "private.220.61.242",
				"private243 (WR2 privateZEVO3)": "private.220.61.243",
				"private244 (WR2 privateZEVO4)": "private.220.61.244",
				"private245 (WR2 privateZEVO5)": "private.220.61.245",
				"private246 (WR2 privateZEVO6)": "private.220.61.246"
			}
		},


}
# template for remmina profile
remminaConfig = {
	"encodings": "",
	"ssh_tunnel_privatekey": "privateWWWe",
	"name": "",
	"password": "privatelQWZYZ",
	"quality": "X",
	"disablesmoothscrolling": "X",
	"precommand": "",
	"ssh_tunnel_enabled": "X",
	"labels": "",
	"ssh_tunnel_command": "",
	"assistance_mode": "0",
	"viewonly": "0",
	"disableserverinput": "0",
	"aspect_ratio": "",
	"postcommand": "",
	"tightencoding": "0",
	"server": "",
	"disablepasswordstoring": "0",
	"ignore-tls-errors": "1",
	"ssh_tunnel_username": "",
	"disconnect-prompt": "0",
	"disableclipboard": "0",
	"disableserverbell": "0",
	"ssh_tunnel_password": "",
	"profile-lock": "0",
	"showcursor": "0",
	"disableencryption": "0",
	"group": "",
	"ssh_tunnel_loopback": "0",
	"colordepth": "32",
	"notes_text": "",
	"ssh_tunnel_auth": "0",
	"enable-autostart": "0",
	"ssh_tunnel_certfile": "",
	"keymap": "",
	"ssh_tunnel_server": "",
	"proxy": "",
	"ssh_tunnel_passphrase": "",
	"protocol": "VNC",
	"username": "tvs",
	"viewmode": "1",
	"window_width": "640",
	"window_maximize": "0",
	"window_height": "480"
}

def generateRemmina(hostname):
	"""exit the template and write to the local folder.

	:Str hostname: The name of computer
	"""
	for tvsName, tvsIp in labTVSip[hostname]["tvs"].items():
		oFilePath = filePath.replace("tvsName", tvsName).replace("tvsIp", tvsIp.replace(".", "-"))
		remminaConfig["name"] = tvsName
		remminaConfig["server"] = tvsIp + PORT
		f = open(oFilePath, "w")
		f.write("[remmina]" + "\n")
		for rconfig, rvalue in remminaConfig.items():
			f.write(rconfig + "=" + rvalue + "\n")
		f.close()

def setNetwork(hostname, ifName):
	"""Just linux command to add the ip and gateway.

	:Str hostname: The name of computer
	:Str ifName: The name of network interface
	"""
	subprocess.run(["ip", "addr", "add", labTVSip[hostname]["ip"] + "/24", "dev", ifName])
	subprocess.run(["ip", "route", "add", "default", "via", labTVSip[hostname]["route_default"], "dev", ifName])

if __name__ == "__main__":

	# Getting inputs
	print("hostname?")
	hostname = str(input()).upper()
	print("Interface Name?")
	ifName = str(input()).lower()
	if hostname and ifName:
		generateRemmina(hostname)
		setNetwork(hostname, ifName)
		print("Saving changes.. please wait until the process finished!")
		subprocess.run(["savechanges"])
		print("finished")
	else:
		print("Strings empty")