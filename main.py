import nmap3
scan = nmap3.Nmap()
version_result = scan.nmap_version_detection("192.168.0.1")
for i in version_result["192.168.0.1"]["ports"]:
    print(i["portid"], i["state"], i["service"])


