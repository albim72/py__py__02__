import socket
import json


def handle_request(data: str):
    """Obsługuje żądania w formacie JSON."""
    try:
        request = json.loads(data)
        command = request.get("command")

        if command == "ping":
            response = {"response": "pong"}
        elif command == "echo":
            message = request.get("message", "")
            response = {"response": message}
        else:
            response = {"error": "Unknown command"}
    except json.JSONDecodeError:
        response = {"error": "Invalid JSON"}

    return json.dumps(response)


def run_server(host='127.0.0.1', port=5000):
    """Uruchamia serwer TCP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(5)
        print(f"Serwer nasłuchuje na {host}:{port}")

        while True:
            client, addr = server.accept()
            with client:
                data = client.recv(1024).decode('utf-8')
                if not data:
                    continue
                response = handle_request(data)
                client.sendall(response.encode('utf-8'))


if __name__ == "__main__":
    run_server()
