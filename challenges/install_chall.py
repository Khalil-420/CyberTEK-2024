import os,glob

categories = ["web","crypto","forensics","misc","pwn","reverse"]

for category in categories:
    if os.path.exists(f"./{category}"):
        challenges = glob.glob(f"{category}/*")
        for challenge in challenges:
            print(f"[+] Installing challenge: {category}/{challenge}")
            os.system(f"python3 -m ctfcli challenge add \"{category}/{challenge}\" && python3 -m ctfcli challenge install \"{category}/{challenge}\"")    
    else:
        print(f"[-] Cant find : {category}")
        exit(1)

exit(0)