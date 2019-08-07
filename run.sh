docker build -t docker-blender:2.8-cpu -f Dockerfile.cpu .
docker run --rm -v $(pwd)/media/:/media/ docker-blender:2.8-cpu