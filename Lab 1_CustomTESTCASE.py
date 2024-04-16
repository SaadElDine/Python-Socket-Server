import socket

def test_server(host, port):
    while True:
        try:
            # Connect to the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))

                # Get user input
                request = input("Enter a string to send to the server (or type 'exit' to quit): ")
                if request.lower() == 'exit':
                    break

                # Send request to server
                s.sendall(request.encode('utf-8'))

                # Receive and print server response
                response = s.recv(1024)
                print('Received:', response.decode('utf-8'))

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    HOST = 'localhost'  # Server's hostname or IP address
    PORT = 7370         # Port used by the server

    test_server(HOST, PORT)
