#!/bin/bash
awslocal lambda invoke --endpoint http://localhost:4566 --function-name ToDoApiStack-lambda-8bf6e52b /tmp/output.txt --region us-east-1 --payload '{"uuid":"b3fd766b-c2aa-4943-8c8b-268d37dea0ff"}'

cat /tmp/output.txt 

count=$(cat /tmp/output.txt | grep "b3fd766b-c2aa-4943-8c8b-268d37dea0ff" | wc -l)

if [ "$count" -eq "1" ]; then
    echo "Passed" #Count should be 1, because all to-do's have Universally Unique ID
else
    echo "Something went wrong, please check the payload or search string"
fi