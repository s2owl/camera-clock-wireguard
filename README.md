# camera-clock

Clock first
https://learn.adafruit.com/adafruit-led-backpack/1-2-inch-7-segment-backpack-assembly

Camera second

cat /etc/motioneye/motion.conf
check if the last line contains: input -1 if not add it and then run
sudo service motion restart

run top
find both motion PID and kill both
run sudo service motioneye start
