FROM python:3.8

ARG prj_dir="/txt2txt/"

WORKDIR $prj_dir

RUN apt-get update \
    && apt-get install -y \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt $prj_dir

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt \
    && rm -r ~/.cache/pip

COPY . $prj_dir