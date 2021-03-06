FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update -y

# gcc compiler and opencv prerequisites
RUN apt-get -y install nano git build-essential libglib2.0-0 libsm6 libxext6 libxrender-dev sudo cmake ninja-build

# Detectron2 prerequisites
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install cython
RUN pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

RUN pip install -U 'git+https://github.com/facebookresearch/fvcore'

RUN python -m pip install detectron2==0.4 -f \
  https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.6/index.html

# Detectron2 - CPU copy
#RUN python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/index.html
#RUN python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.6/index.html
# Development packages
#RUN git clone https://github.com/facebookresearch/detectron2 detectron2_repo
#RUN pip install -e detectron2_repo
RUN pip install numpy pandas pynrrd pillow scikit-image jedi==0.17.2 opencv-python-headless

COPY gen_metadata.py .
COPY ./config ./config
COPY ./output ./output

COPY gen_meta_script.sh .
RUN chmod +x gen_meta_script.sh

ENTRYPOINT ["./gen_meta_script.sh"]
CMD ["Data/Images"]
