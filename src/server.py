import socket
import time
import sys
import platform
import os
import datetime
uname = platform.uname()
host = '0.0.0.0'
print('\n' * 1000)
port = 1337

current_time = datetime.datetime.now()
print(f'[{str(current_time.hour)}:{str(current_time.minute)}:{str(current_time.second)}] Listening on {port}...')

while True:
    try:
        with socket.socket() as s:

            s.bind((host, port))


            s.listen()

            con, addr = s.accept()
            current_time = datetime.datetime.now()
            print(f'[{str(current_time.hour)}:{str(current_time.minute)}:{str(current_time.second)}] {addr} - Gained Connection.')
            with con:
                def send_string(string):
                    con.sendall(bytes(string, "utf-8"))
                while True:
                    data = con.recv(1024)

                    if not data:
                        current_time = datetime.datetime.now()
                        print(f'[{str(current_time.hour)}:{str(current_time.minute)}:{str(current_time.second)}] {addr} - Lost Connection.')
                        break

                    command = str(data, 'utf-8')
                    if command == "help":
                        response = """\u001b[38;5;200m
..................List Of Commands..................\u001b[0m
help - Displays this message
info - Displays machine information
echo [message] - Display a message in the server terminal
$[command] - Run a command on the machine
disconnect - Disconnect from the Server\u001b[38;5;200m
....................................................\u001b[0m
"""
                        send_string(response)

                    elif command == "info":
                        
                        response = f"""\u001b[38;5;200m
.......Server System Info.......\u001b[0m
System\t\t:\t{uname.system}
Node Name\t:\t{uname.node}
Release\t\t:\t{uname.release}
Version\t\t:\t{uname.version}
Machine\t\t:\t{uname.machine}
Processor\t:\t{uname.processor}\u001b[38;5;200m
................................\u001b[0m
"""
                        send_string(response)

                    elif command.startswith('echo'):
                        if len(command) <= 5:
                            send_string('Usage: echo [message]')
                        else:
                            message = command.replace('echo ', '', 1)
                            current_time = datetime.datetime.now()
                            wall = f"""

[{str(current_time.hour)}:{str(current_time.minute)}:{str(current_time.second)}] Message From {addr}: {message}

    """
                            send_string(wall)
                            print(wall)


                    elif command.startswith('$'):
                        command = command.replace('$', '', 1)
                        if not command:
                            send_string('Usage: $[command]')
                        else:
                            stream = os.popen(command)
                            output = stream.read()
                            send_string(output)



                    else:
                        response = f'Unkown command: {command}'
                        con.sendall(bytes(response, "utf-8"))

    except KeyboardInterrupt:
        quit()

    except:
        pass
