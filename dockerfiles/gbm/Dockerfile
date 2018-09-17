FROM jupyter/scipy-notebook

USER root

RUN apt-get update && \
    apt-get -y upgrade

# Install LightGBM, XGBoost, CatBoost
RUN conda update -n base conda && \
    conda install -y -c conda-forge lightgbm && \
    conda install -y -c anaconda py-xgboost && \
    conda install -y -c conda-forge catboost
