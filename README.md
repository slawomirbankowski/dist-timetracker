cd ./backend
docker build -t timetracker .

cd ./timetracker-ui
docker image build -t timetracker-ui:0.0.1 .


