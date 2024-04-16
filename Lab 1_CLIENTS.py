import socket

def test_server(host, port, test_cases):
    for test_case in test_cases:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((host, port))

                request = test_case["input"]
                print('Test Case: ', request)
                expected_output = test_case["expected_output"]

                # Send request to server
                s.sendall(request.encode('utf-8'))

                # Receive and print server response
                response = s.recv(1024)
                print('Received:', response.decode('utf-8'))
                print('Expected Output: ', expected_output)

                # Verify response
                if response.decode('utf-8') == expected_output:
                    print("Test Passed!")
                else:
                    print("Test Failed!")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    HOST = 'localhost'  # Server's hostname or IP address
    PORT = 7370         # Port used by the server

    test_cases = [
        {"input": "Wpython Socket Server", "expected_output": "The number of words is 3"},
        {"input": "LpythonSocketServer", "expected_output": "The number of lowercase letters is 16"},
        {"input": "UPYTHONSOCKETSERVER", "expected_output": "The number of uppercase letters is 18"},
        {"input": "R1234567890", "expected_output": "The number of numeric characters is 10"},
        {"input": "TpythonSocketServer123", "expected_output": "The total number of characters is 22"},
        {"input": "pythonSocketServer123", "expected_output": "pythonSocketServer123"}
    ]

    test_server(HOST, PORT, test_cases)
