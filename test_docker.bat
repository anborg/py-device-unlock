::docker build -f Dockerfile_pythonzeep -t python-zeep .
::docker run -v C:/dev_space/pyp/device:/apps/deviceops python-zeep /bin/bash -c "ls /apps/deviceops/input/* | wc -l"
::docker run -v C:/dev_space/pyp/device:/apps/deviceops python-zeep /bin/bash -c "ls /apps/deviceops/input/* | python /apps/deviceops/stream_device_ops.py"

::docker run -v C:/dev_space/pyp/device:/apps/deviceops python-zeep /bin/bash -c "ls /apps/deviceops/input/* | python /apps/deviceops/stream_device_ops.py | python /apps/deviceops/deviceservice.py "

::docker run -v C:/dev_space/pyp/device:/apps/deviceops python-zeep /bin/bash -c "/apps/deviceops/test_parse.sh"


docker run -v C:/dev_space/pyp/device:/apps/deviceops python-zeep /bin/bash -c "cd /apps/deviceops; cp done/*.dat input/; ls -d input/* | python stream_device_ops.py | python deviceservice.py"
