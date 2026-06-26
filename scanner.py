# scan_vuln_port
import socket
import requests


target = input("Entrez le site à scanner (ex: example.com) : ")

print("\n--- Scan en cours ---\n")


def scan_port(port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))
        print(f"[+] Port {port} ouvert")
        sock.close()
    except:
        print(f"[-] Port {port} fermé")

print("Scan des ports courants...")
for port in [80, 443, 22]:
    scan_port(port)


print("\nVérification HTTPS...")
try:
    response = requests.get("https://" + target)
    print("[+] HTTPS disponible")
except:
    print("[-] HTTPS non disponible")


print("\nRecherche page admin...")
try:
    response = requests.get("http://" + target + "/admin")
    if response.status_code == 200:
        print("[+] Page /admin trouvée !")
    else:
        print("[-] Page /admin non trouvée")
except:
    print("Erreur lors de la requête")

print("\n--- Scan terminé ---")

