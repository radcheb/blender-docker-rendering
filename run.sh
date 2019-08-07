# CPU verison
docker build -t docker-blender:2.8-cpu -f Dockerfile.cpu .
docker run --rm -v $(pwd)/media/:/media/ docker-blender:2.8-cpu

if [ -x nvidia-smi ]; then
	# GPU verison
	docker build -t docker-blender:2.8-gpu -f Dockerfile.gpu .
	docker run --rm --runtime nvidia -v $(pwd)/media/:/media/ docker-blender:2.8-gpu
fi