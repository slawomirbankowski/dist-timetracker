#!/usr/bin/env sh

set -e

DB_HOST=$1
DB_NAME=$2
DB_USER=$3
env;
echo . $PGPASSFILE .
cat $PGPASSFILE
ls -halt $PGPASSFILE

HAS_DB=$(psql -w -U $DB_USER -h $DB_HOST -d $DB_NAME -a -t -c "select 1 from pg_database where datname = '$DB_NAME'")
if [ ! "$HAS_DB" ]; then
  echo "Creating database $DB_NAME"
  psql -w -U $DB_USER -h $DB_HOST -d $DB_NAME -a -t -c "create database $DB_NAME"
else
  echo "Database already exists"
fi
