FROM pl31/debian-mongodb
RUN mkdir -p /data/db/
RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install python-pip
RUN apt-get install curl
RUN pip install nose
RUN pip install -U mock
RUN pip install pymongo
CMD ["/bin/bash"]
