import time
import picamera
import datetime as dt
import socket
import commands
import sys

with picamera.PiCamera() as camera:
        camera.resolution = (1000, 600)
	camera.framerate = 27
	camera.vflip=True
	camera.hflip=True
	camera.start_preview()
    	camera.annotate_background = picamera.Color('black')
    	camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	timestamp=dt.datetime.now().strftime('%Y%m%d_%H:%M:%S')
	addr=commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]
	camera.start_recording('%s_%s_%s.h264' % (str(sys.argv[1]), timestamp, (addr)))
    	start = dt.datetime.now()
	stptime = int(sys.argv[2])
    	while (dt.datetime.now() - start).seconds < stptime:
        	camera.annotate_text = str(sys.argv[1]) + '_' + dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        	camera.wait_recording(0.2)
    
    	camera.stop_recording()
    	camera.stop_preview()
