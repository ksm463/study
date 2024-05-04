#!/bin/bash

curl -X 'POST' \
  'http://127.0.0.1:8000/event/new' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoicmVhZGVyQHBhY2t0LmNvbSIsImV4cGlyZXMiOjE3MTE0MjI0MjcuNDI2MzQ5Nn0.rgx8QqWk8IF-Go71g-4XzcUjq8fqCNaNWyeLBbajAzg' \
  -H 'Content-Type: application/json' \
  -d '{"title": "FastAPI Book Launch",
  "image": "https://linktomyimage.com/image.png",
  "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
  "tags": ["python", "fastapi", "book", "launch"],
  "location": "Google Meet"
  }'
