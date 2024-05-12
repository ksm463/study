#!/bin/bash

curl -X 'POST' \
  'http://127.0.0.1:8000/user/signin' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=reader%40packt.com&password=examplary&scope=&client_id&client_secret='