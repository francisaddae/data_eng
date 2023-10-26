FROM python:3.9.18

WORKDIR /data_eng

ADD ./requirements.txt /data_eng/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /data_eng/requirements.txt

ADD . .

CMD [ "python", "/data_eng/data_flow/basic_elt.py" ]