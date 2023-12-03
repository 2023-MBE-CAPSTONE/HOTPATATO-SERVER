FROM python:3.11

COPY . /hot-potato-server						
WORKDIR /hot-potato-server	

RUN pip install pipenv
RUN pipenv install --dev --system --deploy
RUN find /usr -name '*.pyc' -delete

CMD ["python","./app.py"]