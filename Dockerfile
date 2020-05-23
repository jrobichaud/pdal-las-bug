FROM pdal/pdal:latest
RUN sudo apt update && sudo apt install -y python3-pip
RUN pip3 install numpy cython packaging
RUN pip3 install PDAL==2.2.2
