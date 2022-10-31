# Dockerfile. image. Container
FROM python:3.10.6

ADD ona_data_ingestion.py .
ADD compose1.env .

RUN pip install requests
RUN pip install python-dotenv

CMD [ "python", "./ona_data_ingestion.py"]