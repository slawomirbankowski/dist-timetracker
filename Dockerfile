FROM python:3.11-slim

ARG POSTGRES_DRIVER_VERSION=42.7.3

RUN groupadd -g 1337 timetracker && \
    useradd -u 1337 -m -g timetracker timetracker && \
    mkdir /app && \
    chown -R timetracker:timetracker /app && \
    chmod 771 /app

RUN apt-get update && \
    apt-get install -y curl gcc python3-dev && \
    mkdir driver && \
    curl https://repo1.maven.org/maven2/org/postgresql/postgresql/${POSTGRES_DRIVER_VERSION}/postgresql-${POSTGRES_DRIVER_VERSION}.jar > driver/postgresql.jar

USER 1337
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache --user -r requirements.txt

ENV JDBC_HOST='undefined'
ENV JDBC_NAME='undefined'
ENV JDBC_URL='undefined'
ENV JDBC_USER_FILE='undefined'
ENV JDBC_PASS_FILE='undefined'
ENV JDBC_DRIVER='org.postgresql.Driver'

ENTRYPOINT ["python", "app.py"]