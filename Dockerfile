FROM python:3.12
WORKDIR /backend_convert

COPY . ./
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]