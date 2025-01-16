def lambda_handler(event, context):
    num1 = event.get('num1')
    num2 = event.get('num2')
    result = num1 + num2
    return {'statusCode': 200, 'body': f'Result: {result}'}
