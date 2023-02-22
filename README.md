# camera-clock

Wiring - https://hackster.imgix.net/uploads/attachments/408336/pyowmclock_breadboard_wWTN3jzSar.png?auto=compress%2Cformat&w=740&h=555&fit=max Note I didnd bother with the temp sensor.

Clock first
<sudo apt-get update
sudo apt-get upgrade
sudo apt-get upgrade -y
sudo apt-get install python3-pip -y
sudo apt-get install python3-pil -y
sudo pip3 install --upgrade setuptools
sudo pip3 install adafruit-circuitpython-ht16k33>

All the clock info and wiring can be found here: https://learn.adafruit.com/adafruit-led-backpack/1-2-inch-7-segment-backpack 

Camera second

cat /etc/motioneye/motion.conf
check if the last line contains: input -1 if not add it and then run
sudo service motion restart

run top
find both motion PID and kill both
run sudo service motioneye start
