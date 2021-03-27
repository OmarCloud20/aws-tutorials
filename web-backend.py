#******************************************************************************************
# Author - Nirmallya Mukherjee
# This lambda function will act as the backend for the loadbalancer and must be in a separate
# target group. You need to ensure that the healthcheck is enabled.
# NOTE: turn healthy. Must have the path in LB as /lambda/
# Modified by Omar A Omar
#******************************************************************************************

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
        "Content-Type": "text/html; charset=utf-8"
        }
    }

    response['body'] = """
    <html>
        <head>
            <title>Hello Lambda!</title>
            <style>
                html, body {
                margin: 0; padding: 0;
                font-family: arial; font-weight: 10; font-size: 1em;
                text-align: center;
            }
            </style>
        </head>
        <body>
            <h1>Hello Friend!</h1>

            <p> My Web-Backend Lambda </p>

        </body>
    </html>
    """

    return response
