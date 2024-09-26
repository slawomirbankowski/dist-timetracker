cd ./backend
docker build -t timetracker .

cd ./timetracker-ui
docker image build -t timetracker-ui:0.0.1 .


docker run -p 8090:8090 -d timetracker-ui:0.0.3