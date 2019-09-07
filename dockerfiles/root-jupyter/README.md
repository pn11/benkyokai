# ROOT-Jupyter

- Docker Hub [pn11/root-jupyter](https://hub.docker.com/r/pn11/root-jupyter)

jupyter/scipy-notebook に ROOT をビルドして足すので割と時間かかる。

以下のように ROOT のイメージに jupyter を入れたほうが早そうだけどまだできていない。

```Dockerfile
FROM rootproject/root-ubuntu

RUN apt-get update && \
    apt-get -y install jupyter

RUN jupyter kernelspec install /usr/local/etc/root/notebook/kernels/root/

# Jupyter のポート番号変更とrootユーザーでの実行許可
## これやってもポート番号が変わらず詰む。
## https://root-forum.cern.ch/t/root-notebook-question-port-and-ip-parameter/29617
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py  && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /root/.jupyter/jupyter_notebook_config.py

