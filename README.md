#build the docker image
`docker build -t my-postgres-image .`

#run the docker container
`docker run -d --name my-postgres-container -e POSTGRES_USER=PG_USER -e POSTGRES_PASSWORD=PG_PASSWORD -e POSTGRES_DB=PG_DATABASE -p 5432:5432 my-postgres-image`


#verify the conytainer is running
`docker ps`

#test the connection
`psql -h localhost -U vboss -d streambix`










