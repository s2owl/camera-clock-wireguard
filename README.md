# Camera-Clock-Wireguard

Objective: I want a have a IR camera using Motioneye and an Adafruit 1.2" clock connected to one Ras Pi Zero W.
OS: Bullseye 32bit
Disclaimer: I found that sometimes some of the updates / upgrades eventually timed out so I had to repeat them.  You need to keep an eye out for this.

Wiring - https://hackster.imgix.net/uploads/attachments/408336/pyowmclock_breadboard_wWTN3jzSar.png?auto=compress%2Cformat&w=740&h=555&fit=max Note I didn't bother with the temp sensor.

## Clock First
```
  sudo apt-get update && sudo apt-get upgrade -y
  sudo apt-get install ntp
  sudo apt-get install python3-pip -y
  sudo apt-get install python3-pil -y
  sudo pip3 install --upgrade setuptools
  sudo pip3 install adafruit-circuitpython-ht16k33
```
Download the above scripts and check it out

All the clock info and wiring can be found here: https://learn.adafruit.com/adafruit-led-backpack/1-2-inch-7-segment-backpack 
Then I made it a service by following this: https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

Before you head off to the Camera - There's a bit more:

### NTP

Edit this file
```
  /etc/ntp.conf
```
I added:
```
  pool 0.uk.pool.ntp.org iburst
  pool 1.uk.pool.ntp.org iburst
  pool 2.uk.pool.ntp.org iburst
  pool 3.uk.pool.ntp.org iburst
```

Restart the service and check its running with:
```
  sudo service ntp restart
  sudo service ntp status
```

## Camera Second

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

### Unable to load video resource
```
  sudo vi cat /etc/motioneye/motion.conf
```
On the last line add `input -1`
```
  sudo vi cat /etc/motioneye/camera-1.conf
```
Find `videodevice /dev/video10` *note* it could be any number really.  Change it to: `videodevice /dev/video0`
```
  sudo service motion restart
```
# Now to remotely manage the device(s)
