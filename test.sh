PROCESS_DIR=/apps/unlock
#PROCESS_DIR=/home/imeiadmin/new_deviceop_dropdir
rm $PROCESS_DIR/logs/*.log 2>/dev/null
cp /apps/unlock/inputBak/*.dat $PROCESS_DIR/input/ 2>/dev/null
/apps/unlock/run.sh
