1. Inside the root directory run
```shell
$ docker build -t timetracker:0.0.1 .
```
2. Inside `deploy` directory create the following files:
   1. `pg-server-user.secret` - containing user used by postgres server,
   e.g. `postgres`
   2. `pg-server-pass.secret` - containing password used by postgres user,
   e.g. `password123`
   
   The whole contents of these files will be used, including
   any trailing newlines.
3. Run `docker-compose up`

After startup the timetracker API will be available
at `0.0.0.0:8000/api`, e.g. `localhost:8000/api/service/ping`.

Postgres DB will be available at `localhost:5433/timetracker`.