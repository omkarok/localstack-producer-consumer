from aws_cdk import core as cdk
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda
from aws_cdk import aws_dynamodb as dynamodb


# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class ToDoApiStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        to_do_table = dynamodb.Table.from_table_arn(self, "to_do_table", "arn:aws:dynamodb:us-east-1:000000000000:table/ToDoTable")
        read_todo = aws_lambda.Function(self, "read_todo_lambda_function",
                                              runtime=aws_lambda.Runtime.PYTHON_3_8,
                                              handler="read_todo.lambda_handler",
                                              code=aws_lambda.Code.asset("./to_do_api/read-todo/"))

        read_todo.add_environment("TABLE_NAME", to_do_table.table_name)

        # grant permission to lambda to read from demo table
        to_do_table.grant_read_data(read_todo)
