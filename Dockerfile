FROM python:3.11.2-slim-bullseye

ENV PROJECT_DIR=/app
ENV PYTHONPATH /app

RUN apt update && apt -y upgrade
RUN apt install -y sqlite3 libsqlite3-dev gcc  # Zainstaluj obsługę SQLite

WORKDIR $PROJECT_DIR

COPY ./requirements.txt $PROJECT_DIR/requirements.txt
RUN pip install -r $PROJECT_DIR/requirements.txt

COPY ./ /app/

RUN chmod +x /app/run_dev_server.sh

CMD ["./run_dev_server.sh"]