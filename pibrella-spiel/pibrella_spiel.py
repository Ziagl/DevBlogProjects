import random
import time
import pibrella

#initialisieren der arrays
leds = [0,1,2]
times = [0.1,0.2,0.3,0.4,0.5]

#Spielschleife
while True:
	select = random.choice(leds)
	if select == 0:
		pibrella.light.green.on()
		time.sleep(random.choice(times))
		pibrella.light.green.off()
	if select == 1:
		pibrella.light.yellow.on()
		time.sleep(random.choice(times))
		pibrella.light.yellow.off()
	if select == 2:
		pibrella.light.red.on()
		time.sleep(random.choice(times))
		pibrella.light.red.off()

	#pruefen ob der button geklickt wirde
	pressed = pibrella.button.read()

	#pruefen ob sieg oder niederlage
	if pressed:
		if select == 0:
			pibrella.buzzer.success()
			pibrella.lights.on()
			time.sleep(3)
			pibrella.buzzer.off()
			pibrella.lights.off()
		else:
			pibrella.buzzer.fail()
			time.sleep(3)
			pibrella.buzzer.off()
