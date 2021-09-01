from socket import *

request = input("Taranıcak Adres: ")
ip = gethostbyname(request)
print("taranıcak ip: {}".format(ip))
        
for i in range(9999):

    connection = socket(AF_INET,SOCK_STREAM)
    scan = connection.connect_ex((ip,i))
    
    if scan == 0:
        print("kullanılan portlar: {} ".format(i))
        connection.close()
        
input("tarama sonlandırıldı.")
