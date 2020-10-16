## Build

docker build -t NAMEOFTHEDOK -f ./Dockerfile .

## Run

docker run -d -p 8000:8080 NAMEOFTHEDOK

##  Stop

docker ps
docker stop ID OF THE DOCK