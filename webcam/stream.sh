#!/bin/sh
 
# mjpg-streamer start script
 
# Path to mjpg_streamer and libraries
export LD_LIBRARY_PATH="/home/pi/Documents/mjpg-streamer"
STREAMER="$LD_LIBRARY_PATH/mjpg_streamer"
 
# Pi camera configurations
XRES="640x"
YRES="480"
FPS="10"
 
# Web configurations
WWWDOC="$LD_LIBRARY_PATH/www"
PORT="8080"
USER="user"
PASS="password"
 
# Start streaming
$STREAMER -i "input_uvc.so -r $XRES$YRES -y -f $FPS" \
          -o "output_http.so -w $WWWDOC -p $PORT"

#./mjpg_streamer -i "./input_uvc.so -f 10 -r 320x240 -d /dev/video0 -y -n" -o "./output_http.so -w ./www -p 8080"
