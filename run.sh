#!/bin/bash

APP_PID=
stopRunningProcess() {
    if test ! "${APP_PID}" = '' && ps -p ${APP_PID} > /dev/null ; then
        echo "Stopping Streamlit app with process ID ${APP_PID}" > /proc/1/fd/1
        kill -TERM ${APP_PID}
        echo "Waiting for Streamlit to process SIGTERM signal" > /proc/1/fd/1
        wait ${APP_PID}
        echo "All processes have stopped running" > /proc/1/fd/1
    else
        echo "Streamlit was not running or already stopped" > /proc/1/fd/1
    fi
}

trap stopRunningProcess EXIT TERM

source ${VIRTUAL_ENV}/bin/activate

streamlit run ${HOME}/app/main.py --server.address=0.0.0.0 &
APP_PID=$!

wait ${APP_PID}
