from ubuntu

ENV DEBIAN_FRONTEND noninteractive
run apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python python-pip vim && \
    apt-get install -y mysql-server libmysqlclient-dev && \
    pip install -U pip && \
    pip install PyMySQL MySQL-python alembic

add requirements.txt /root/requirements.txt
run pip install -r /root/requirements.txt

add json-diff.py /root/json-diff.py
add xls-to-json.py /root/xls-to-json.py
run chmod +x /root/json-diff.py /root/xls-to-json.py
