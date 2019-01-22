import boto3
import json
from os import path


from utils import Utils


LAMBDA_ROLE = 'Lambda_Execution_Role'
LAMBDA_ACCESS_POLICY_ARN = 'arn:aws:iam::018837131763:policy/LambdaS3AccessPolicy'
LAMBDA_ROLE_ARN = 'arn:aws:iam::018837131763:role/Lambda_Execution_Role'
LAMBDA_TIMEOUT = 10
LAMBDA_MEMORY = 128
PYTHON_3_RUNTIME = 'python3.7'
PYTHON_LAMBDA_NAME = 'PythonLambdaFunction'
LAMBDA_HANDLER = 'lambda_function.handler'
NODEJS_RUNTIME = 'nodejs8.10'
NODEJS_LAMBDA_NAME = 'NodeJSLambdaFunction'
AWS_REGION = 'us-east-1'


def lambda_client():
	""" :type : pyboto3.lambda """
	aws_lambda = boto3.client('lambda', region_name = AWS_REGION)
	return aws_lambda


def iam_client():
	iam = boto3.client('iam')
	""" : type : pyboto3.iam """
	return iam


def create_access_policy_for_lambda():
	s3_access_policy_document = {
		"Version": "2012-10-17",
		"Statement": [
			{
				"Action": [
					"s3:*",
					"logs:CreateLogGroup",
					"logs:CreateLogStream",
					"logs:PutLogEvents"
				],
				"Effect": "Allow",
				"Resource": "*"
			}
		]
	}	

	return iam_client().create_policy(
		PolicyName = 'LambdaS3AccessPolicy',
		PolicyDocument = json.dumps(s3_access_policy_document),
		Description = 'Allows lambda functions to access S3 resources'
	)


def create_execution_role_for_lambda():
	lambda_execution_assumption_role = {
		"Version": "2012-10-17",
		"Statement": [
			{
				"Effect": "Allow",
				"Principal": {
					"Service":"lambda.amazonaws.com"
				},
				"Action":"sts:AssumeRole"		
			}
		]
	}


	return iam_client().create_role(
			RoleName = LAMBDA_ROLE,
			AssumeRolePolicyDocument = json.dumps(lambda_execution_assumption_role),
			Description = 'Gives necessary permissions for lambda execution'
		)	


def attach_access_policy_to_execution_role():
	return iam_client().attach_role_policy(
			RoleName = LAMBDA_ROLE,
			PolicyArn= LAMBDA_ACCESS_POLICY_ARN
	)


def deploy_lambda_function(function_name, runtime, handler, role_arn, source_folder):
	folder_path = path.join(path.dirname(path.abspath(__file__)), source_folder)
	zip_file = Utils.make_zip_file_bytes(path=folder_path)


	return lambda_client().create_function(
		FunctionName = function_name,
		Runtime = runtime,
		Role = role_arn,
		Handler = handler,
		Code = {
			'ZipFile': zip_file

		},
		Timeout = LAMBDA_TIMEOUT,
		MemorySize = LAMBDA_MEMORY,
		Publish = False
	)



def invoke_lambda_function(function_name):
	return lambda_client().invoke(FunctionName = function_name)


def add_environment_variables_to_lambda(function_name, var):
	return lambda_client().update_function_configuration(
		FunctionName = function_name,
		Environment = var
	)


def publish_new_version(function_name):
	return lambda_client().publish_version(
		FunctionName = function_name
	)


def create_alias_for_new_version(function_name, alias_name, version):
	return lambda_client().create_alias(
		FunctionName = function_name,
		Name = alias_name,
		FunctionVersion = version,
		Description = 'This is the ' + alias_name + 'alias for function'
	)


def invoke_lamda_with_alias(function_name, alias_name):
	return lambda_client().invoke(
		FunctionName = function_name,
		Qualifier = alias_name
	)


def get_function(function_name):
	return lambda_client().get_function(FunctionName=function_name)


def get_all_functions():
	return lambda_client().list_functions()


def increase_lambda_execution_memory(function_name, new_memory_size):
	return lambda_client().update_function_configuration(
		FunctionName = function_name,
		MemorySize = new_memory_size
	)


def delete_lambda_function(function_name):
	return lambda_client().delete_function(FunctionName=function_name)


