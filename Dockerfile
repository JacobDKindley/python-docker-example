FROM python

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN pip install -e .

CMD [ "python", "-m", "pytest", "./tests" ]