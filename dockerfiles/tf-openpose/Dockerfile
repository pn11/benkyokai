FROM python:3.5

RUN apt-get update && \
    apt-get install -y git wget gzip

RUN git clone https://www.github.com/ildoonet/tf-openpose && \
    cd tf-openpose && \
    pip3 install -r requirements.txt && \
    pip3 install opencv-python tensorflow && \
    python setup.py install
