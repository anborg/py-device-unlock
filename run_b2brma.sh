#!/usr/bin/env bash
PROCESS_DIR=/apps/Unlock
SRC_DIR=/apps/Unlock/Source
cd $SRC_DIR && ls -d $PROCESS_DIR/Inbound/*B2BRMAnotification*.dat 2>/dev/null | python36 stream_device_ops.py | python36 deviceservice.py
