from ubuntu

run apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python python-pip && \
    pip install -U pip
add requirements.txt /root/requirements.txt
run pip install -r /root/requirements.txt

add dump.py /root/dump.py
add master.conf /root/master.conf
add slave.conf /root/slave.conf
run chmod +x /root/dump.py
