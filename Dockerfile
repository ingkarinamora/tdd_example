FROM frolvlad/alpine-python3
RUN apk update && apk upgrade
RUN apk add bash python git
RUN easy_install nose
RUN easy_install -U mock
RUN mkdir /home/tdd_example
ADD app /home/tdd_example/app
ADD test /home/tdd_example/test
ADD __init__.py /home/tdd_example/__init__.py
CMD ["/bin/bash"]
