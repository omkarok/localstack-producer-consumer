#!/bin/bash
awslocal lambda invoke --endpoint http://localhost:4566 --function-name ToDoApiStack-lambda-8bf6e52b /tmp/output.txt --region us-east-1 && cat /tmp/output.txt