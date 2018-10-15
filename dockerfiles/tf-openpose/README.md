# README

Just run https://github.com/ildoonet/tf-pose-estimation in Docker.

## Build

```
docker build -t tf-openpose tf-openpose
```

## Run

```
docker run -it -e DISPLAY=10.0.75.1:0.0 tf-openpose bash
```

In the container,

```
cd tf-openpose
python run.py --model=mobilenet_thin --resize=432x368 --image=./images/p1.jpg
```

Python のバージョンが3.7だと pip に TensorFlow が入ってなかった？
