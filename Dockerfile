FROM python:3.8
#Используем образ python 3.8

#Выбераем рабочую директорию нашего проекта
WORKDIR /app

#копируем нужные нам зависимости и помещаем в раб деректорию
COPY ./req .

ENV VIRTUAL_ENV=/app/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin/:$PATH"

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r ./req
COPY . .

CMD ["uvicorn", "app.main:app ", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:6500"]