FROM ubuntu
MAINTAINER chinniprashanth <chinniprashanth001@gmail.com>
RUN apt-get update -y \
&& apt-get install python -y \
&& apt-get update \
&& apt install python-pip -y \
&& pip install requests \
&& apt-get install vim curl wget -y 
WORKDIR /root/
COPY /mac.py /root 
ENTRYPOINT ["python", "./mac.py"]
