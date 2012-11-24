#!/bin/bash
cmd="python project/manage.py celeryd -B --settings=envs.live"
$cmd &
sleep 10
ps aux | grep 'manage.py celeryd' | awk '{print $2}' | xargs kill -TERM




