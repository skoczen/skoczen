#!/bin/bash
cmd="./manage.py celeryd -B "
$cmd &
sleep 10
ps aux | grep 'manage.py celeryd' | awk '{print $2}' | xargs kill -TERM




