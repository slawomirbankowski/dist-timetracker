ARG POSTGRES_DRIVER_VERSION=42.7.3

FROM python:3.11-slim as driver_downloader
RUN apt-get update && \
    apt-get install -y curl && \
    mkdir /driver && \
    curl https://repo1.maven.org/maven2/org/postgresql/postgresql/${POSTGRES_DRIVER_VERSION}/postgresql-${POSTGRES_DRIVER_VERSION}.jar > /driver/postgresql.jar

RUN apt-get install net-tools

FROM python:3.11-slim

RUN groupadd -g 1337 timetracker && \
    useradd -u 1337 -m -g timetracker timetracker && \
    mkdir /app && \
    chown -R timetracker:timetracker /app && \
    chmod 771 /app

RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-17-jdk curl


USER 1337
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache --user -r requirements.txt
USER root
COPY . /app/
COPY --from=driver_downloader /driver/postgresql.jar /app/
RUN chown -R timetracker:timetracker /app
USER 1337

ENV JDBC_HOST='undefined'
ENV JDBC_NAME='undefined'
ENV JDBC_URL='undefined'
ENV JDBC_USER_FILE='undefined'
ENV JDBC_PASS_FILE='undefined'
ENV JDBC_DRIVER='org.postgresql.Driver'

CMD ["python", "main.py"]