# Building and deploying in docker hub
docker build -t failuremanager .
docker tag failuremanager californibrs/failuremanager
docker push californibrs/failuremanager