FROM python:3.9.18

WORKDIR /data_eng

COPY ./requirements.txt /data_eng/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /data_eng/requirements.txt

COPY ./data_flow /data_eng/data_flow

CMD [ "python", "/data_eng/data_flow/basic_elt.py" ]