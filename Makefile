# You must configure this Makefile to suit your solution
DIR=$(shell pwd)

all:
	docker run -it --rm \
	  --env DISPLAY=${DISPLAY} --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	  -v=$(DIR)/..:$(DIR)/.. -w=$(DIR) \
	  adnrv/opencv \
	  python $(DIR)/src/hw0.py;
	echo Running p0-XX-YY
