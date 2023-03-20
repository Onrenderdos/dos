import socket
import random
import time

UDP_IP = "91.133.76.97"  # IP-Adresse des Zielhosts
UDP_PORT = 80  # Portnummer des Zielhosts
MESSAGE_SIZE = 1024 * 1024  # Größe der zu sendenden Nachricht (1 MB)

# Erstelle das UDP-Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sende die Nachricht in einer Schleife
while True:
    # Generiere eine zufällige Nachricht mit der angegebenen Größe
    message = bytearray(random.getrandbits(8) for _ in range(MESSAGE_SIZE))

    # Sende die Nachricht an die Ziel-IP und den Zielport
    sock.sendto(message, (UDP_IP, UDP_PORT))

    # Warte 1 Sekunde
    time.sleep(1)
