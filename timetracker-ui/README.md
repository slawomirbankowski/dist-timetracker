# TimeTracker UI

cd ./backend
docker build -t timetracker .

cd ./timetracker-ui
docker image build -t timetracker-u .


docker run -p 8090:8090 -d timetracker-ui
