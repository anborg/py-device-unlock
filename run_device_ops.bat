SET INPUT_DIR=C:/dev_space/pyp/device/input
SET SRC_DIR=C:/dev_space/pyp/device/src
rm  "%INPUT_DIR%/../logs/*.log"
cp %INPUT_DIR%/../done/*.dat %INPUT_DIR%/
(ls -d %INPUT_DIR%/*.dat | python %SRC_DIR%/stream_device_ops.py | python %SRC_DIR%/deviceservice.py )