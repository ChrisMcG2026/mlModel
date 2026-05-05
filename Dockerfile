FROM python:3.11
EXPOSE 5001
WORKDIR /opt/app2
COPY . /opt/app2
RUN pip3.11 install -r requirements.txt
RUN python3.11 model.py
CMD ["python3.11", "/opt/app2/flaskApp.py"]

