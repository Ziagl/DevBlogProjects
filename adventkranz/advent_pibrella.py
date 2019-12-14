import pibrella
import datetime

#aktuelle Zeit holen
now = datetime.datetime.now()
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
		pibrella.output.e.on()
	if(now >= zweiter_advent):
		pibrella.output.f.on()
	if(now >= dritter_advent):
		pibrella.output.g.on()
	if(now >= vierter_advent):
		pibrella.output.h.on()

input("Programm wir mit Tastendruck beendet")
