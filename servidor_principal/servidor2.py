
from socket import socket
try:
    raw_input
except NameError:
    raw_input = input
def main():
    s = socket()
    s.connect(("localhost",6031))
    
    while True:
        output_data = raw_input("> ")
        
        if output_data:
            try:
                s.send(output_data)
            except TypeError:
                s.send(bytes(output_data, "utf-8"))
            input_data = s.recv(1024)
            if input_data:
               
                print(input_data.decode("utf-8") if
                      isinstance(input_data, bytes) else input_data)
if __name__ == "__main__":
    main()