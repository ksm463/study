#!/bin/bash

curl -X 'POST' \
  'http://127.0.0.1:8000/user/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "email": "reader@packt.com","password": "exemplary","events": []
  }'