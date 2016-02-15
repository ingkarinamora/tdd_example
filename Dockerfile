FROM pl31/debian-mongodb
RUN mkdir -p /data/db/
RUN mkdir /home/tdd_example
ADD app /home/tdd_example/app
ADD test /home/tdd_example/test
ADD __init__.py /home/tdd_example/__init__.py
RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install python-pip
RUN apt-get install curl
RUN pip install nose
RUN pip install -U mock
CMD ["/bin/bash"]
