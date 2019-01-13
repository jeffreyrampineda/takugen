# Takugen

Key press character translator

## Requirements

* docker 18.03.1-ce or later

## Build

``` bash
docker build --tag=takugen .
```

## Run

``` bash
docker run --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" takugen:latest
```