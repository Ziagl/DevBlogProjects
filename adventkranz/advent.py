import RPi.GPIO as GPIO
import datetime

#initialisiere GPIO
PIN_A = 7
PIN_B = 8
PIN_C = 10
PIN_D = 11
GPIO.setmode(GPIO.BOARD)

#aktuelle Zeit holen
now = datetime.datetime(2014,12,24,0,0,0)#datetime.datetime.now()
#Datum extrahieren
jahr = now.year
monat = now.month
tag = now.day
#Debugausgabe aktuelles Datum
#print "Es ist der %02i.%02i.%04i" % (tag,monat,jahr)

#Wochentag von Weihnachten bestimmen
weihnachten = datetime.datetime(jahr, 12, 24, 0, 0, 0)
wochentag = weihnachten.weekday()
vierter_advent = weihnachten - datetime.timedelta(wochentag + 1)
dritter_advent = weihnachten - datetime.timedelta(wochentag + 8)
zweiter_advent = weihnachten - datetime.timedelta(wochentag + 15)
erster_advent = weihnachten - datetime.timedelta(wochentag + 22)

#Debugausgabe aktuelles Datum
#print "1. Adventsonntag: %02i.%02i.%04i" % (erster_advent.day,erster_advent.month,erster_advent.year)
#print "2. Adventsonntag: %02i.%02i.%04i" % (zweiter_advent.day,zweiter_advent.month,zweiter_advent.year)
#print "3. Adventsonntag: %02i.%02i.%04i" % (dritter_advent.day,dritter_advent.month,dritter_advent.year)
#print "4. Adventsonntag: %02i.%02i.%04i" % (vierter_advent.day,vierter_advent.month,vierter_advent.year)

#LEDS aktivieren basierend auf Datum
if(now <= weihnachten):
	if(now >= erster_advent):
		GPIO.setup(PIN_A, GPIO.OUT)
		GPIO.output(PIN_A, True)
	if(now >= zweiter_advent):
		GPIO.setup(PIN_B, GPIO.OUT)
		GPIO.output(PIN_B, True)
	if(now >= dritter_advent):
		GPIO.setup(PIN_C, GPIO.OUT)
		GPIO.output(PIN_C, True)
	if(now >= vierter_advent):
		GPIO.setup(PIN_D, GPIO.OUT)
		GPIO.output(PIN_D, True)

a = raw_input("Programm wir mit Tastendruck beendet")
GPIO.cleanup()

