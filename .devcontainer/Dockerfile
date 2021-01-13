FROM python:3.9.1-slim
COPY --chown=root:root docker_hello.py /root/
RUN python /root/docker_hello.py
RUN pip install --upgrade pip
RUN python -m pip install \
        numpy \
        pandas_datareader \
        pandas \
        matplotlib \
        sklearn
