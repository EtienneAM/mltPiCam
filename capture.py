import time
import picamera
import datetime as dt
import socket
import commands
import sys

with picamera.PiCamera() as camera:
        camera.resolution = (1920, 1080)
	camera.framerate = 30
	#camera.vflip=True #vertical flip
	#camera.hflip=True #horizontal flip

	camera.start_preview() 
    	camera.annotate_background = picamera.Color('black')

    	camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
	timestamp=dt.datetime.now().strftime('%Y%m%d_%H:%M:%S:%f')

	addr=commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:] #finds local ip address
	camera.start_recording('%s_%s.h264' % (str(sys.argv[1]), socket.gethostname())) #starts recording and names file with 
    	start = dt.datetime.now()
	stptime = int(sys.argv[2])
    	while (dt.datetime.now() - start).seconds < stptime:
        	camera.annotate_text = str(sys.argv[1]) + '_' + socket.gethostname() + '_' + dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        	camera.wait_recording(0.2)
    
    	camera.stop_recording()
    	camera.stop_preview()
