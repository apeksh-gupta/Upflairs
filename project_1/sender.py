import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = '127.0.0.1'
port = 9999


target_ip = (ip, port)
message = input('Write your message: ')
file_name = input('Enter the name of the file you want to send : ')
encryptred_message = message.encode('ascii')

# s.sendto(encryptred_message, target_ip)

with open(f'{file_name}', 'rb') as file :
    data = file.read()
    s.sendto(data, target_ip)

print('File sent successfully')
data = s.recvfrom(120)
print(data)