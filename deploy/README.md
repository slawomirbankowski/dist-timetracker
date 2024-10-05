1. Inside `deploy` directory create the following files:
   1. `pg-server-user.secret` - containing user used by postgres server,
   e.g. `postgres`
   2. `pg-server-pass.secret` - containing password used by postgres user,
   e.g. `password123`
   3. `elasticsearch-pass.secret` - containing password used by Elasticsearch,
   e.g. `password123`
   4. `redis-pass.secret` - containing password used by Redis,
   e.g. `password123`

   The whole contents of these files will be used, including
   any trailing newlines.


2. Inside the deploy directory run

```shell
cd ../timetracker-backend
docker build -t timetracker:1.1.0 .
cd ../timetracker-ui
docker build -t timetracker-ui:1.0.0 .
cd ../deploy
docker-compose up

```
3. Run `docker-compose up`

After startup the timetracker API will be available
at `0.0.0.0:8000/api`, e.g. `localhost:8000/api/service/ping`.

Postgres DB will be available at `localhost:5433/timetracker`.
