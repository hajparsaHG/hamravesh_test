FROM hub.hamdocker.ir/python:3.10

WORKDIR /app/
ADD . /app/
RUN pip install -r ./requirements.txt
RUN pip install --upgrade pip

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

