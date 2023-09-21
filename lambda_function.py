import json
from text_comparison import compare_text


def lambda_handler(event, context):
    """Lambda function that handles incoming requests for file comparison."""
    request_body = json.loads(event['body'])

    text1 = request_body['text1']
    text2 = request_body['text2']

    change_info = compare_text(text1, text2)

    return_data = []

    for change_item in change_info:
        temp_dict = dict()
        temp_dict['character'] = change_item.data
        temp_dict['status'] = change_item.change_type

        return_data.append(temp_dict)

    return {
        'statusCode': 200,
        'body': json.dumps(return_data, indent=4)
    }
