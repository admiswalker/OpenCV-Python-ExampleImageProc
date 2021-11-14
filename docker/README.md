# docker-opencv-python

## Usage
### Building the dockerfile
```
$ cd docker
$ ./docker_build.sh
```
### Running the sample code of `./docker/main.py`
- Method 1. Entering the docker image console and running `./docker/main.py`
  ```
  $ cd docker
  $ ./docker_run_with_console.sh
  # python3 main.py
  # 4.2.0
  ```
- Method 2. Running `./docker/main.py` directory
  ```
  $ cd docker
  $ ./docker_run_with_console.sh
  4.2.0
  ```

## How to install openCV into docker
Let's see [Install OpenCV-Python in Ubuntu](https://docs.opencv.org/3.4/d2/de6/tutorial_py_setup_in_ubuntu.html).


## Trouble shooting
- To avoid the installation option of `Time Zone`, enable the following options.
  ```
  ENV DEBIAN_FRONTEND=noninteractive
  ```

