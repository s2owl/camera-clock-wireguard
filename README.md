# Camera-Clock

Wiring - https://hackster.imgix.net/uploads/attachments/408336/pyowmclock_breadboard_wWTN3jzSar.png?auto=compress%2Cformat&w=740&h=555&fit=max Note I didn't bother with the temp sensor.

## Clock first
```
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get upgrade -y
  sudo apt-get install python3-pip -y
  sudo apt-get install python3-pil -y
  sudo pip3 install --upgrade setuptools
  sudo pip3 install adafruit-circuitpython-ht16k33
```

All the clock info and wiring can be found here: https://learn.adafruit.com/adafruit-led-backpack/1-2-inch-7-segment-backpack 

Then I made it a service by following this: https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

## Camera second

Based on this: https://github.com/motioneye-project/motioneye/wiki/Install-on-Raspbian-Bullseye
As i said earlier - this is for a ras pi zero so is a 32bit OS, the above link has the 64bit version

```
   sudo -i
   apt-get install ffmpeg libmariadb3 libpq5 libmicrohttpd12 -y
   wget https://github.com/Motion-Project/motion/releases/download/release-4.3.2/pi_buster_motion_4.3.2-1_armhf.deb 
   dpkg -i pi_buster_motion_4.3.2-1_armhf.deb 
   systemctl stop motion
   systemctl disable motion 
```
The next block has to be entered one at a time.  No exceptions.
```
  apt-get install python2 python-dev-is-python2 -y

  curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py

  python2 get-pip.py

  apt-get install libssl-dev libcurl4-openssl-dev libjpeg-dev zlib1g-dev -y
```

```
  pip2 install motioneye
  mkdir -p /etc/motioneye
  cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf
  mkdir -p /var/lib/motioneye
  cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
  systemctl daemon-reload
  systemctl enable motioneye
  systemctl start motioneye
```
note: If pillow installation fails (hangs and ends at 99%),
you can install it from official repos using
`apt-get install python-pil -y`
and rerun
`pip2 install motioneye`

cat /etc/motioneye/motion.conf
check if the last line contains: input -1 if not add it and then run
sudo service motion restart

run top
find both motion PID and kill both
run sudo service motioneye start
