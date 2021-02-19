:: SET DSBASE_PATH=C:/dev_space/pyp/device
:: ls %DSBASE_PATH%/input/*.* | python %DSBASE_PATH%/stream_device_ops.py


SET PROCESS_DIR=C:/dev_space/pyp/device
SET SRC_DIR=%PROCESS_DIR%/Source
mkdir %PROCESS_DIR%/Inbound 2>/dev/null
rm %PROCESS_DIR%/logs/*.log 2>/dev/null
cp %PROCESS_DIR%/inputBak/*.dat %PROCESS_DIR%/Inbound/ 2>/dev/null
ls -d %PROCESS_DIR%/Inbound/* | python %SRC_DIR%/stream_device_ops.py
