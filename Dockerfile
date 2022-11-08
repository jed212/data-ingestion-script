# Dockerfile. image. Container
FROM python:3.10.6
WORKDIR /new_csv_file

COPY ona_data_ingestion.py .
COPY compose1.env .

RUN pip install requests
RUN pip install python-dotenv

CMD [ "python", "./ona_data_ingestion.py"]