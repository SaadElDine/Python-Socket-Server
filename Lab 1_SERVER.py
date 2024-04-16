import socketserver

class MyRequestHandler_7370(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            # Receive data from the client and decode it
            data = self.request.recv(1024).strip().decode('utf-8')
            # Extract the operation code (first character) and the text (remaining characters)
            operation = data[0]
            text = data[1:]

            # Perform the requested operation based on the operation code
            if operation == 'W':
                count = len(text.split())
                response = f"The number of words is {count}"
            elif operation == 'L':
                count = sum(1 for c in text if c.islower())
                response = f"The number of lowercase letters is {count}"
            elif operation == 'U':
                count = sum(1 for c in text if c.isupper())
                response = f"The number of uppercase letters is {count}"
            elif operation == 'R':
                count = sum(1 for c in text if c.isdigit())
                response = f"The number of numeric characters is {count}"
            elif operation == 'T':
                count = len(text)
                response = f"The total number of characters is {count+1}"
            else:
                # If the operation code is not recognized, return the text as is
                response = data

            # Send the response back to the client
            self.request.sendall(response.encode('utf-8'))

        except Exception as e:
            # Handle any exceptions that occur during processing
            error_message = f"An error occurred: {str(e)}"
            self.request.sendall(error_message.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 7370

    # Create a TCP server instance with the custom request handler
    server = socketserver.TCPServer((HOST, PORT), MyRequestHandler_7370)

    try:
        # Start the server to handle incoming connections
        server.serve_forever()
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (Ctrl+C) to gracefully shutdown the server
        print("Server shutdown requested.")
        server.shutdown()
        server.server_close()  # Close the server socket
