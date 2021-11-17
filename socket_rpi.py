#! /usr/bin/env python
import socket
import serial

serial_Arduino = serial.Serial('/dev/ttyACM0',9600)
serial_Arduino.flushInput()
socket_s = socket.socket()
host =''
port = 9999
backlog = 5
socket_s.bind ((host,port))
socket_s.listen(backlog)

print "ESPERANDO UNA CONEXION ... :|"
socket_s, (host,port) = socket_s.accept()
print "CONEXION ESTABLECIDA ..... :)"

while True:
	try:
		if(serial_Arduino.inWaiting() > 0):
			sArduino = serial_Arduino.readline()
			datos = sArduino.rstrip('\n')
			socket_s.send(datos)
	except:
		print "DESCONECTADO ............. :("
		socket_s.close()
		break


# Ruben Loredo Amaro
# https://www.youtube.com/user/rubyck71
# Septiembre  2017
