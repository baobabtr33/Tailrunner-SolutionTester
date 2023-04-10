docker login

docker build --platform linux/arm -t testcode:0.6 .
docker tag testcode:0.6 stevekim01310/testcode:0.6
docker push stevekim01310/testcode:0.6

sudo docker pull stevekim01310/testcode:0.6
sudo docker run --platform linux/arm64 -it -p 9000:9000 --rm stevekim01310/testcode:0.6
