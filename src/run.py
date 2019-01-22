from lambda_app import *


if __name__ == '__main__':
	# print(create_access_policy_for_lambda())



	# print(create_execution_role_for_lambda())
	


	# print(attach_access_policy_to_execution_role())	
	


	# print(deploy_lambda_function(PYTHON_LAMBDA_NAME, 
	# 	PYTHON_3_RUNTIME, 
	# 	LAMBDA_HANDLER, 
	# 	LAMBDA_ROLE_ARN, 
	# 	'python_lambda')
	# )

	# print(deploy_lambda_function(NODEJS_LAMBDA_NAME, 
	# 	NODEJS_RUNTIME, 
	# 	LAMBDA_HANDLER, 
	# 	LAMBDA_ROLE_ARN, 
	# 	'nodejs_lambda')
	# )


	# response = invoke_lambda_function(PYTHON_LAMBDA_NAME)
	# output = response['Payload'].read().decode()
	# print(output)



	## add environment virables
	# env_variables = {
	# 	'Variables': {
	# 		'ENV_VAR_TEST': 'this is an env variable'
	# 	}
	# }
	# add_environment_variables_to_lambda(PYTHON_LAMBDA_NAME, env_variables)


	## publish a version
	# pub_ver = publish_new_version(PYTHON_LAMBDA_NAME)
	# print(pub_ver)


	## add an alias
	# create_alias_for_new_version(PYTHON_LAMBDA_NAME, 'PROD', '1')


	## invoke lambda function
	# p = invoke_lamda_with_alias(PYTHON_LAMBDA_NAME, 'PROD')
	# print(p['Payload'].read().decode())


	## get function config info
	# config_info = get_function(PYTHON_LAMBDA_NAME)
	# print(config_info)


	## print the list of all available functions
	# function_list = get_all_functions()
	# print(function_list)

	## invoke function to increase the function memory size
	# increase_lambda_execution_memory(PYTHON_LAMBDA_NAME, 256)


	## invoke function to delete NodeJS Lambda function
	# delete_lambda_function(NODEJS_LAMBDA_NAME)	







