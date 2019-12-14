import re
import os
import time
import datetime

directory = "/sys/bus/w1/devices/"
log = "temperature.log"

#finde alle angeschlossenen 1-wire Geraete
devices = os.listdir(directory)

for f in devices:
	if f != "w1_bus_master1":
		file = open(directory+f+"/w1_slave")
		line = file.readline()
		if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES",line):
			line = file.readline()
			m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)",line)
			if m:
				value = str(float(m.group(2)) / 1000.0)
		#print "Measured temperature from "+f+": "+value
		logfile = open(log, 'a')
		ts = time.time()
		timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d.%m.%Y %H:%M:%S')
		logfile.write(timestamp+" "+value+"\n")
		logfile.close()
		file.close()
