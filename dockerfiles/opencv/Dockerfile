FROM ubuntu_dev_minimal

# Download opencv
RUN git clone https://github.com/opencv/opencv.git && \
    cd opencv && \
    git checkout tags/3.4.2 && \
    mkdir build 

# Download opencv_contrib
RUN git clone https://github.com/opencv/opencv_contrib.git && \
    cd opencv_contrib && \
    git checkout tags/3.4.2

# Build OpenCV with contribution modules
RUN cd opencv/build && \
    cmake -DOPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules .. && \
    make -j2 && \
    make install
    