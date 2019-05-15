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

# ROOT の Jupyter Kernel を Jupyter にインストール
RUN runuser jovyan -c "jupyter kernelspec install --user /home/jovyan/root/etc/notebook/kernels/root/;"
RUN pip install metakernel

ENV ROOTSYS /usr/local
ENV LD_LIBRARY_PATH /usr/local/lib
ENV DYLD_LIBRARY_PATH /usr/local/lib
ENV CMAKE_PREFIX_PATH /usr/local
ENV JUPYTER_PATH /usr/local/etc/notebook
ENV SHLIB_PATH /usr/local/lib
ENV LIBPATH /usr/local/lib
ENV PYTHONPATH /usr/local/lib
ENV MANPATH /usr/local/man:
ENV CLING_STANDARD_PCH none

CMD runuser jovyan -c "jupyter notebook"

# 不要データ削除
RUN rm -r /home/jovyan/root /home/jovyan/root-build
