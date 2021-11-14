FROM ubuntu:20.04

COPY requirements.txt .

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get upgrade

RUN apt-get install -y libopencv-dev \
    	    	       python3-opencv \
    	    	       python3-numpy

RUN apt-get install -y libpng-dev \
    	    	       libjpeg-dev \
		       libopenexr-dev \
		       libtiff-dev \
		       libwebp-dev

RUN apt-get install -y pip \
    && pip install -r requirements.txt

