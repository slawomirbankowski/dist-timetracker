# dist-timetracker
Planning 
pip install psycopg2
pip install pyliquibase
pip install flask

curl https://repo1.maven.org/maven2/org/postgresql/postgresql/${POSTGRES_DRIVER_VERSION}/postgresql-${POSTGRES_DRIVER_VERSION}.jar > /driver/postgresql.jar

docker build -t timetracker .
set $env:POSTGRES_DRIVER_VERSION=42.7.3

docker build -t timetracker .
docker build -t timetracker:1.0.0 .

docker-compose -f .\docker-compose.yaml start
set $env:APP_HOST=localhost
set $env:POSTGRES_USER=timetracker
set $env:POSTGRES_DB=timetracker


ALTER ROLE timetracker SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN REPLICATION NOBYPASSRLS;

docker-compose -f .\docker-compose.yaml up


