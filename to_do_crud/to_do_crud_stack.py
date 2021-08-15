from aws_cdk import core as cdk

from aws_cdk import aws_dynamodb as dynamodb

from aws_cdk import aws_lambda
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class ToDoCrudStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        to_do_table = dynamodb.Table(self, "to_do_table", table_name="ToDoTable",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING)
        )

        create_todo = aws_lambda.Function(self, "create_todo_lambda_function",
                                              runtime=aws_lambda.Runtime.PYTHON_3_8,
                                              handler="create_todo.lambda_handler",
                                              code=aws_lambda.Code.asset("./to_do_crud/create-todo/"))

        create_todo.add_environment("TABLE_NAME", to_do_table.table_name)

        # grant permission to lambda to write to demo table
        to_do_table.grant_write_data(create_todo)

