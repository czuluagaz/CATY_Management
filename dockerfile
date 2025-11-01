# Dockerfile
# create a dockerfile for the CATY sql lite database, the python version is 3.11, the database is sqlite
# the database is stored in the /caty directory

FROM alpine:latest

# install SQLite
RUN apk --no-cache add sqlite

# create a directory for the database
RUN mkdir /caty
RUN mkdir /caty/db

# copy the database file to the directory
COPY ../../CATY_MANAGEMENT/db/caty_sql /caty/db

# Expose the port
EXPOSE 1433e'

# set the working directory
WORKDIR /caty

# run the database
CMD ["sqlite3", "/caty/db/caty_sql"]

