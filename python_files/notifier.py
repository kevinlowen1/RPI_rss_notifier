from datetime import datetime
import boto3
import config

def notify(rawList):
    client = boto3.client(
                'sns'
                ,aws_access_key_id=config.AWSAccessKeyId
                ,aws_secret_access_key=config.AWSAccessKey
                ,region_name = config.regionToUse
            )

    for i in rawList:
        # print(i[2])
        client.publish( 
            TopicArn= 'arn:aws:sns:us-east-1:583893304007:raspberryPiZeroStockAlerts'
            ,Message= i[2]
            ,Subject= 'raspberryPiStockAlert'
        )


if __name__ == "__main__":
    inputs = [[9, datetime(2022, 4, 1, 22, 24, 41), 'Stock Alert (US): Raspberry Pi Zero 2 W is In Stock at Sparkfun']]
    notify(inputs)