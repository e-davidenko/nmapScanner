import nmap3

scan = nmap3.Nmap()
version_result = scan.nmap_version_detection("192.168.0.1")
for i in version_result["192.168.0.1"]["ports"]:
    print("Номер порта:", i["portid"], ", состояние порта:", i["state"], ", имя службы:", i["service"]["name"], ", версия:", i["service"].get('version', '-'))
