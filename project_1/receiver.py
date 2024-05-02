import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # defining way and protocol
ip = '127.0.0.1'
port = 9999  # from 0 to 65536

complete_address = (ip, port)
s.bind(complete_address)

while True:
    data = s.recvfrom(120)  # NO. OF CHARACTERS IT CAN RECEIVE AT A TIME
   
    # message = data[0]
    # decrypted_msg = message.decode('ascii') + '\n'
    # sender_ip = data[1][0]
    # file_name = sender_ip + '.txt'
    # with open(f'{file_name}', 'a+') as file :  # advance append mode
    #     file.write(f'{decrypted_msg}')

    file_data = data[0]
    sender_ip = data[1][0]
    with open('received.txt', 'wb') as file:
        file.write(file_data)

    
    print('File received successfully')
    # reply_msg = 'Thanks for this file'
    # reply = reply_msg.encode('ascii')
    # s.sendto(reply, sender_ip)
        
        

# IP address of our systems+
# 127.0.0.1
# 0.0.0.0
