BASE_DIR=/apps/deviceops
docker run -v $BASE_DIR:$BASE_DIR python-zeep /bin/bash -c "cd $BASE_DIR; cp done/*.dat Inbound/; ls -d Inbound/* | python stream_device_ops.py | python deviceservice.py"
