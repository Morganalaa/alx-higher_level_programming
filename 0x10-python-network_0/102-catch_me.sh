#!/bin/bash
#  Bash script that makes a request to 0.0.0.0:5000/catch_me  response "You got me!"
curl -sX PUT -L -d "user_id=98" --header "You got me!" 0.0.0.0:5000/catch_me
