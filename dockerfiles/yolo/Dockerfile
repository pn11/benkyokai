FROM opencv

RUN apt-get install -y pkg-config

RUN git clone https://github.com/pjreddie/darknet && \
    cd darknet && \
    sed -i -e "s/OPENCV=0/OPENCV=1/g" Makefile && \
    make -j2 && \
    wget https://pjreddie.com/media/files/yolov3.weights
    