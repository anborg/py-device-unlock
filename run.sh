PROCESS_DIR=/apps/Unlock
SRC_DIR=/apps/Unlock/Source
cd $SRC_DIR && ls -d $PROCESS_DIR/Inbound/* | python36 stream_device_ops.py | python36 deviceservice.py
