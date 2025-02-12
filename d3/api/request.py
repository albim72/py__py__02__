import socket
import json


def send_request(command, message=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("127.0.0.1", 5000))
        request = {"command": command}
        if message:
            request["message"] = message
        client.sendall(json.dumps(request).encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print("Odpowiedź:", response)


send_request("ping")
send_request("echo", "Witaj, świecie!")
