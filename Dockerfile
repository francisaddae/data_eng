FROM python:3.10

ADD requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ADD . .

CMD [ "python", "/data_eng/data_flow/basic_elt.py" ]