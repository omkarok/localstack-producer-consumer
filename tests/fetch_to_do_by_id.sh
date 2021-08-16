#!/bin/bash
awslocal lambda invoke --endpoint http://localhost:4566 --function-name ToDoApiStack-lambda-69354cc1 /tmp/output.txt --region us-east-1 --payload '{"uuid":"546b764e-aa0a-489c-a7a3-1c4f5b1e32da"}'

cat /tmp/output.txt 

count=$(cat /tmp/output.txt | grep "546b764e-aa0a-489c-a7a3-1c4f5b1e32da" | wc -l)

if [ "$count" -eq "1" ]; then
    echo "Passed" #Count should be 1, because all to-do's have Universally Unique ID
else
    echo "Something went wrong, please check the payload or search string"
fi