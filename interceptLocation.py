import socket
import struct
import geoip2.database
import requests
def ipv4(raw_data):
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])
    src = '.'.join(map(str,src))
    target = '.'.join(map(str,target))
    return (src,target)
def i2l(ip):
	if str(ip).startswith('127.0.') or str(ip).startswith('192.168.'):
		return  i2l(myip)
	try:
		response=reader.city(ip)
		return response.location.latitude,response.location.longitude
	except geoip2.errors.AddressNotFoundError:
		return None
if __name__ == '__main__':
	myip=requests.get('http://ip.jsontest.com/').json()['ip']
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	reader=geoip2.database.Reader('GeoLite2-City.mmdb')
	while True:
		raw_data, addr = conn.recvfrom(65535)
		dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])
		proto = socket.htons(prototype)
		if proto == 8:
			file=open('traffic dump.txt','a')
			ipv4src,ipv4target = ipv4(raw_data[14:])
			sourceLoc=i2l(ipv4src)
			destLoc=i2l(ipv4target)
			#print(1)			
			if sourceLoc is None or destLoc is None:
				continue
			print('IPv4 Packet:')
			print('Source \nip: {} \tlocation:{},\n Target \nip: {} \tlocation:{}'.format(ipv4src,sourceLoc,ipv4target,destLoc))
			if sourceLoc == destLoc:
				continue
			file.write('\n'+str([sourceLoc[1],sourceLoc[0],destLoc[1], destLoc[0]]))
			file.close()
			

