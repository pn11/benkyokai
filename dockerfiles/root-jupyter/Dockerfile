FROM jupyter/scipy-notebook

USER root
#    apt-get -y upgrade && \

# Required Package
# https://root.cern.ch/build-prerequisites#ubuntu
RUN apt-get update && \
    apt-get install -y git dpkg-dev cmake g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev

# ROOT のビルド
# ROOT は rootproject/root-ubuntu16 などのイメージで配布されているが Jupyter が入っていないのでここでは使わない。
# 時間が掛かるが自分でビルドする。
# ここを見て要らなそうなオプションは消す。 https://root.cern.ch/building-root
# ここでは Bonjour とデータベースを OFF にしてみた。
RUN git clone https://github.com/root-project/root.git
# && \
RUN mkdir root-build  && \
    cd root-build && \
    cmake ../root -Dbonjour=OFF -Dmysql=OFF -Doracle=OFF -Dpgsql=OFF && \
    make -j3 && \
    make install

# ROOT の Jupyter Kernel をコピー
# https://github.com/root-project/root/tree/master/bindings/pyroot/JupyROOT
RUN cp -r $ROOTSYS/etc/notebook/kernels/root ~/.local/share/jupyter/kernels
