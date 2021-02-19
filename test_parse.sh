#PROCESS_DIR=/home/imeiadmin/new_deviceop_dropdir
PROCESS_DIR=/apps/Unlock
SRC_DIR=/apps/Unlock/Source
mkdir $PROCESS_DIR/Inbound 2>/dev/null
rm $PROCESS_DIR/logs/*.log 2>/dev/null
cp /apps/Unlock/inputBak/*.dat $PROCESS_DIR/Inbound/ 2>/dev/null
cd $SRC_DIR && ls -d $PROCESS_DIR/Inbound/* | python36 stream_device_ops.py
