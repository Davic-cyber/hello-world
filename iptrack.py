import requests
print('Welcome brothers !!!!')
import socket
import sys, ipaddress
#third party public ip
public = 'http://httpbin.org/ip'
ip_api= 'http://ip-api.com/json/{0}'
static_ip= socket.gethostbyname(socket.gethostname())
public_ip= requests.get(public).json()['origin']
def Ip_vaild(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False
try:
    ip = str(sys.argv[1])
    if not Ip_vaild(ip):
        ip = socket.gethostbyname(ip)
except IndexError:
    ip =  socket.gethostbyname(socket.gethostname())
def main(ip):
    print('Your Static Ip address : ({0})'.format(static_ip))
    print('Your Public Ip address : ({0})'.format(public_ip))
    data = requests.get(ip_api.format(ip)).json()
    for d in data:
        print(d,' : ',data[d])
    print()
ip= input('Enter the web address to track ip: ')
main(ip)