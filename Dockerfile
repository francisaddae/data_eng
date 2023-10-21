# syntax=docker/dockerfile:1

# base python image for custom image
FROM python:latest

# create working directory and install pip dependencies
WORKDIR /home/app

# run packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# port
EXPOSE 8080

CMD ["python", "*.py"]
