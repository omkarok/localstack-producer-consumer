#!/bin/bash
for i in {1..5}; do awslocal lambda invoke --endpoint http://localhost:4566 --function-name ToDoCrudStack-lambda-3cbdf4c2 --payload '{"title":"'$i'","task":"Automated Tests"}' /tmp/output.txt --region us-east-1; done

awslocal dynamodb scan --table-name ToDoTable > /tmp/output.txt #To overwrite the temp file at every test run

count=$(cat /tmp/output.txt | grep "Automated Tests" | wc -l)
echo $count
if [ "$count" -eq "5" ]; then
    echo "Passed"
else
    echo "Something went wrong, please check the payload or search string"
fi