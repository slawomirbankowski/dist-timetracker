# TimeTracker UI

cd ./timetracker-ui

docker build -t timetracker-ui .
docker run --name timetracker-ui -p 8090:8090 -d timetracker-ui
