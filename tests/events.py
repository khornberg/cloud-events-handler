s3_example_event = {
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-2",
            "eventTime": "2019-09-03T19:37:27.192Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {"principalId": "AWS:AIDAINPONIXQXHT3IKHL2"},
            "requestParameters": {"sourceIPAddress": "205.255.255.255"},
            "responseElements": {
                "x-amz-request-id": "D82B88E5F771F645",
                "x-amz-id-2": "vlR7PnpV2Ce81l0PRw6jlUpck7Jo5ZsQjryTjKlc5aLWGVHPZLj5NeC6qMa0emYBDXOo6QBU0Wo=",
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "828aa6fc-f7b5-4305-8584-487c791949c1",
                "bucket": {
                    "name": "lambda-artifacts-deafc19498e3f2df",
                    "ownerIdentity": {"principalId": "A3I5XTEXAMAI3E"},
                    "arn": "arn:aws:s3:::lambda-artifacts-deafc19498e3f2df",
                },
                "object": {
                    "key": "b21b84d653bb07b05b1e6b33684dc11b",
                    "size": 1305107,
                    "eTag": "b21b84d653bb07b05b1e6b33684dc11b",
                    "sequencer": "0C0F6F405D6ED209E1",
                },
            },
        }
    ]
}

eventbridge_scheduled_example_event = {
    "id": "53dc4d37-cffa-4f76-80c9-8b7d4a4d2eaa",
    "detail-type": "Scheduled Event",
    "source": "aws.events",
    "account": "123456789012",
    "time": "2015-10-08T16:53:06Z",
    "region": "us-east-1",
    "resources": ["arn:aws:events:us-east-1:123456789012:rule/MyScheduledRule"],
    "detail": {},
}

cloudevents = {
    "specversion": "1.0-rc1",
    "type": "com.example.someevent",
    "source": "/my/context",
    "id": "A234-1234-1234",
    "time": "2018-04-05T17:31:00Z",
    "comexampleextension1": "value",
    "comexampleothervalue": 5,
    "datacontenttype": "text/xml",
    "data": '<much wow="xml"/>',
}

alexa_smart_home_event = {
    "header": {"payloadVersion": "1", "namespace": "Control", "name": "SwitchOnOffRequest"},
    "payload": {
        "switchControlAction": "TURN_ON",
        "appliance": {"additionalApplianceDetails": {"key2": "value2", "key1": "value1"}, "applianceId": "sampleId"},
        "accessToken": "sampleAccessToken",
    },
}

cloudtrail_event = {
    "Records": [
        {
            "eventVersion": "1.02",
            "userIdentity": {
                "type": "Root",
                "principalId": "123456789012",
                "arn": "arn:aws:iam::123456789012:root",
                "accountId": "123456789012",
                "accessKeyId": "access-key-id",
                "sessionContext": {"attributes": {"mfaAuthenticated": "false", "creationDate": "2015-01-24T22:41:54Z"}},
            },
            "eventTime": "2015-01-24T23:26:50Z",
            "eventSource": "sns.amazonaws.com",
            "eventName": "CreateTopic",
            "awsRegion": "us-east-2",
            "sourceIPAddress": "205.251.233.176",
            "userAgent": "console.amazonaws.com",
            "requestParameters": {"name": "dropmeplease"},
            "responseElements": {"topicArn": "arn:aws:sns:us-east-2:123456789012:exampletopic"},
            "requestID": "3fdb7834-9079-557e-8ef2-350abc03536b",
            "eventID": "17b46459-dada-4278-b8e2-5a4ca9ff1a9c",
            "eventType": "AwsApiCall",
            "recipientAccountId": "123456789012",
        },
        {
            "eventVersion": "1.02",
            "userIdentity": {
                "type": "Root",
                "principalId": "123456789012",
                "arn": "arn:aws:iam::123456789012:root",
                "accountId": "123456789012",
                "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
                "sessionContext": {"attributes": {"mfaAuthenticated": "false", "creationDate": "2015-01-24T22:41:54Z"}},
            },
            "eventTime": "2015-01-24T23:27:02Z",
            "eventSource": "sns.amazonaws.com",
            "eventName": "GetTopicAttributes",
            "awsRegion": "us-east-2",
            "sourceIPAddress": "205.251.233.176",
            "userAgent": "console.amazonaws.com",
            "requestParameters": {"topicArn": "arn:aws:sns:us-east-2:123456789012:exampletopic"},
            "responseElements": None,
            "requestID": "4a0388f7-a0af-5df9-9587-c5c98c29cbec",
            "eventID": "ec5bb073-8fa1-4d45-b03c-f07b9fc9ea18",
            "eventType": "AwsApiCall",
            "recipientAccountId": "123456789012",
        },
    ]
}

cloudformation_event = {
    "RequestType": "Create",
    "ServiceToken": "arn:aws:lambda:us-east-2:123456789012:function:lambda-error-processor-primer-14ROR2T3JKU66",
    "ResponseURL": "https://cloudformation-custom-resource-response-useast2.s3-us-east-2.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-east-2%3A123456789012%3Astack/lambda-error-processor/1134083a-2608-1e91-9897-022501a2c456%7Cprimerinvoke%7C5d478078-13e9-baf0-464a-7ef285ecc786?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Expires=1555451971&Signature=28UijZePE5I4dvukKQqM%2F9Rf1o4%3D",  # noqa E501
    "StackId": "arn:aws:cloudformation:us-east-2:123456789012:stack/lambda-error-processor/1134083a-2608-1e91-9897-022501a2c456",  # noqa E501
    "RequestId": "5d478078-13e9-baf0-464a-7ef285ecc786",
    "LogicalResourceId": "primerinvoke",
    "ResourceType": "AWS::CloudFormation::CustomResource",
    "ResourceProperties": {
        "ServiceToken": "arn:aws:lambda:us-east-2:123456789012:function:lambda-error-processor-primer-14ROR2T3JKU66",
        "FunctionName": "lambda-error-processor-randomerror-ZWUC391MQAJK",
    },
}


cloudfront_event = {
    "Records": [
        {
            "cf": {
                "config": {"distributionId": "EDFDVBD6EXAMPLE"},
                "request": {
                    "clientIp": "2001:0db8:85a3:0:0:8a2e:0370:7334",
                    "method": "GET",
                    "uri": "/picture.jpg",
                    "headers": {
                        "host": [{"key": "Host", "value": "d111111abcdef8.cloudfront.net"}],
                        "user-agent": [{"key": "User-Agent", "value": "curl/7.51.0"}],
                    },
                },
            }
        }
    ]
}

config_event = {
    "invokingEvent": '{"configurationItem":{"configurationItemCaptureTime":"2016-02-17T01:36:34.043Z","awsAccountId":"000000000000","configurationItemStatus":"OK","resourceId":"i-00000000","ARN":"arn:aws:ec2:us-east-1:000000000000:instance/i-00000000","awsRegion":"us-east-1","availabilityZone":"us-east-1a","resourceType":"AWS::EC2::Instance","tags":{"Foo":"Bar"},"relationships":[{"resourceId":"eipalloc-00000000","resourceType":"AWS::EC2::EIP","name":"Is attached to ElasticIp"}],"configuration":{"foo":"bar"}},"messageType":"ConfigurationItemChangeNotification"}',  # noqa E501
    "ruleParameters": '{"myParameterKey":"myParameterValue"}',
    "resultToken": "myResultToken",
    "eventLeftScope": False,
    "executionRoleArn": "arn:aws:iam::012345678912:role/config-role",
    "configRuleArn": "arn:aws:config:us-east-1:012345678912:config-rule/config-rule-0123456",
    "configRuleName": "change-triggered-config-rule",
    "configRuleId": "config-rule-0123456",
    "accountId": "012345678912",
    "version": "1.0",
}

codecommit_event = {
    "Records": [
        {
            "awsRegion": "us-east-2",
            "codecommit": {
                "references": [{"commit": "5e493c6f3067653f3d04eca608b4901eb227078", "ref": "refs/heads/master"}]
            },
            "eventId": "31ade2c7-f889-47c5-a937-1cf99e2790e9",
            "eventName": "ReferenceChanges",
            "eventPartNumber": 1,
            "eventSource": "aws:codecommit",
            "eventSourceARN": "arn:aws:codecommit:us-east-2:123456789012:lambda-pipeline-repo",
            "eventTime": "2019-03-12T20:58:25.400+0000",
            "eventTotalParts": 1,
            "eventTriggerConfigId": "0d17d6a4-efeb-46f3-b3ab-a63741badeb8",
            "eventTriggerName": "index.handler",
            "eventVersion": "1.0",
            "userIdentityARN": "arn:aws:iam::123456789012:user/intern",
        }
    ]
}

cognito_event = {
    "datasetName": "datasetName",
    "eventType": "SyncTrigger",
    "region": "us-east-1",
    "identityId": "identityId",
    "datasetRecords": {
        "SampleKey2": {"newValue": "newValue2", "oldValue": "oldValue2", "op": "replace"},
        "SampleKey1": {"newValue": "newValue1", "oldValue": "oldValue1", "op": "replace"},
    },
    "identityPoolId": "identityPoolId",
    "version": 2,
}

dynamodb_event = {
    "Records": [
        {
            "eventID": "1",
            "eventVersion": "1.0",
            "dynamodb": {
                "Keys": {"Id": {"N": "101"}},
                "NewImage": {"Message": {"S": "New item!"}, "Id": {"N": "101"}},
                "StreamViewType": "NEW_AND_OLD_IMAGES",
                "SequenceNumber": "111",
                "SizeBytes": 26,
            },
            "awsRegion": "us-west-2",
            "eventName": "INSERT",
            "eventSourceARN": "eventsourcearn",
            "eventSource": "aws:dynamodb",
        },
        {
            "eventID": "2",
            "eventVersion": "1.0",
            "dynamodb": {
                "OldImage": {"Message": {"S": "New item!"}, "Id": {"N": "101"}},
                "SequenceNumber": "222",
                "Keys": {"Id": {"N": "101"}},
                "SizeBytes": 59,
                "NewImage": {"Message": {"S": "This item has changed"}, "Id": {"N": "101"}},
                "StreamViewType": "NEW_AND_OLD_IMAGES",
            },
            "awsRegion": "us-west-2",
            "eventName": "MODIFY",
            "eventSourceARN": "sourcearn",
            "eventSource": "aws:dynamodb",
        },
    ]
}

ec2_lifecycle_event = {
    "version": "0",
    "id": "b6ba298a-7732-2226-xmpl-976312c1a050",
    "detail-type": "EC2 Instance State-change Notification",
    "source": "aws.ec2",
    "account": "123456798012",
    "time": "2019-10-02T17:59:30Z",
    "region": "us-east-2",
    "resources": ["arn:aws:ec2:us-east-2:123456798012:instance/i-0c314xmplcd5b8173"],
    "detail": {"instance-id": "i-0c314xmplcd5b8173", "state": "running"},
}

iot_event = {
    "event": {
        "eventName": "myChargedEvent",
        "eventTime": 1567797571647,
        "payload": {
            "detector": {
                "detectorModelName": "AWS_IoTEvents_Hello_World1567793458261",
                "detectorModelVersion": "4",
                "keyValue": "100009",
            },
            "eventTriggerDetails": {
                "triggerType": "Message",
                "inputName": "AWS_IoTEvents_HelloWorld_VoltageInput",
                "messageId": "64c75a34-068b-4a1d-ae58-c16215dc4efd",
            },
            "actionExecutionId": "49f0f32f-1209-38a7-8a76-d6ca49dd0bc4",
            "state": {"variables": {}, "stateName": "Charged", "timers": {}},
        },
    }
}

kinesis_event = {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49590338271490256608559692538361571095921575989136588898",
                "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
                "approximateArrivalTimestamp": 1545084650.987,
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000006:49590338271490256608559692538361571095921575989136588898",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
            "awsRegion": "us-east-2",
            "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream",
        },
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49590338271490256608559692540925702759324208523137515618",
                "data": "VGhpcyBpcyBvbmx5IGEgdGVzdC4=",
                "approximateArrivalTimestamp": 1545084711.166,
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000006:49590338271490256608559692540925702759324208523137515618",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
            "awsRegion": "us-east-2",
            "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream",
        },
    ]
}

kinesis_firehose_event = {
    "invocationId": "invoked123",
    "deliveryStreamArn": "aws:lambda:events",
    "region": "us-west-2",
    "records": [
        {
            "data": "SGVsbG8gV29ybGQ=",
            "recordId": "record1",
            "approximateArrivalTimestamp": 1510772160000,
            "kinesisRecordMetadata": {
                "shardId": "shardId-000000000000",
                "partitionKey": "4d1ad2b9-24f8-4b9d-a088-76e9947c317a",
                "approximateArrivalTimestamp": "2012-04-23T18:25:43.511Z",
                "sequenceNumber": "49546986683135544286507457936321625675700192471156785154",
                "subsequenceNumber": "",
            },
        },
        {
            "data": "SGVsbG8gV29ybGQ=",
            "recordId": "record2",
            "approximateArrivalTimestamp": 151077216000,
            "kinesisRecordMetadata": {
                "shardId": "shardId-000000000001",
                "partitionKey": "4d1ad2b9-24f8-4b9d-a088-76e9947c318a",
                "approximateArrivalTimestamp": "2012-04-23T19:25:43.511Z",
                "sequenceNumber": "49546986683135544286507457936321625675700192471156785155",
                "subsequenceNumber": "",
            },
        },
    ],
}

lex_event = {
    "messageVersion": "1.0",
    "invocationSource": "FulfillmentCodeHook",
    "userId": "ABCD1234",
    "sessionAttributes": {"key1": "value1", "key2": "value2"},
    "bot": {"name": "my-bot", "alias": "prod", "version": "1"},
    "outputDialogMode": "Text",
    "currentIntent": {
        "name": "my-intent",
        "slots": {"slot-name": "value", "slot-name": "value", "slot-name": "value"},
        "confirmationStatus": "Confirmed",
    },
}

ses_event = {
    "Records": [
        {
            "eventVersion": "1.0",
            "ses": {
                "mail": {
                    "commonHeaders": {
                        "from": ["Jane Doe <janedoe@example.com>"],
                        "to": ["johndoe@example.com"],
                        "returnPath": "janedoe@example.com",
                        "messageId": "<0123456789example.com>",
                        "date": "Wed, 7 Oct 2015 12:34:56 -0700",
                        "subject": "Test Subject",
                    },
                    "source": "janedoe@example.com",
                    "timestamp": "1970-01-01T00:00:00.000Z",
                    "destination": ["johndoe@example.com"],
                    "headers": [
                        {"name": "Return-Path", "value": "<janedoe@example.com>"},
                        {
                            "name": "Received",
                            "value": "from mailer.example.com (mailer.example.com [203.0.113.1]) by inbound-smtp.us-west-2.amazonaws.com with SMTP id o3vrnil0e2ic for johndoe@example.com; Wed, 07 Oct 2015 12:34:56 +0000 (UTC)",  # noqa E501
                        },
                        {
                            "name": "DKIM-Signature",
                            "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=example.com; s=example; h=mime-version:from:date:message-id:subject:to:content-type; bh=jX3F0bCAI7sIbkHyy3mLYO28ieDQz2R0P8HwQkklFj4=; b=sQwJ+LMe9RjkesGu+vqU56asvMhrLRRYrWCbV",  # noqa E501
                        },
                        {"name": "MIME-Version", "value": "1.0"},
                        {"name": "From", "value": "Jane Doe <janedoe@example.com>"},
                        {"name": "Date", "value": "Wed, 7 Oct 2015 12:34:56 -0700"},
                        {"name": "Message-ID", "value": "<0123456789example.com>"},
                        {"name": "Subject", "value": "Test Subject"},
                        {"name": "To", "value": "johndoe@example.com"},
                        {"name": "Content-Type", "value": "text/plain; charset=UTF-8"},
                    ],
                    "headersTruncated": False,
                    "messageId": "o3vrnil0e2ic28tr",
                },
                "receipt": {
                    "recipients": ["johndoe@example.com"],
                    "timestamp": "1970-01-01T00:00:00.000Z",
                    "spamVerdict": {"status": "PASS"},
                    "dkimVerdict": {"status": "PASS"},
                    "processingTimeMillis": 574,
                    "action": {
                        "type": "Lambda",
                        "invocationType": "Event",
                        "functionArn": "arn:aws:lambda:us-west-2:012345678912:function:Example",
                    },
                    "spfVerdict": {"status": "PASS"},
                    "virusVerdict": {"status": "PASS"},
                },
            },
            "eventSource": "aws:ses",
        }
    ]
}

sns_event = {
    "Records": [
        {
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:us-east-2:123456789012:sns-lambda:21be56ed-a058-49f5-8c98-aedd2564c486",  # noqa E501
            "EventSource": "aws:sns",
            "Sns": {
                "SignatureVersion": "1",
                "Timestamp": "2019-01-02T12:45:07.000Z",
                "Signature": "tcc6faL2yUC6dgZdmrwh1Y4cGa/ebXEkAi6RibDsvpi+tE/1+82j...65r==",
                "SigningCertUrl": "https://sns.us-east-2.amazonaws.com/SimpleNotificationService-ac565b8b1a6c5d002d285f9598aa1d9b.pem",  # noqa E501
                "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
                "Message": "Hello from SNS!",
                "MessageAttributes": {
                    "Test": {"Type": "String", "Value": "TestString"},
                    "TestBinary": {"Type": "Binary", "Value": "TestBinary"},
                },
                "Type": "Notification",
                "UnsubscribeUrl": "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&amp;SubscriptionArn=arn:aws:sns:us-east-2:123456789012:test-lambda:21be56ed-a058-49f5-8c98-aedd2564c486",  # noqa E501
                "TopicArn": "arn:aws:sns:us-east-2:123456789012:sns-lambda",
                "Subject": "TestInvoke",
            },
        }
    ]
}

sqs_event = {
    "Records": [
        {
            "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
            "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
            "body": "test",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1545082649183",
                "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                "ApproximateFirstReceiveTimestamp": "1545082649185",
            },
            "messageAttributes": {},
            "md5OfBody": "098f6bcd4621d373cade4e832627b4f6",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
            "awsRegion": "us-east-2",
        },
        {
            "messageId": "2e1424d4-f796-459a-8184-9c92662be6da",
            "receiptHandle": "AQEBzWwaftRI0KuVm4tP+/7q1rGgNqicHq...",
            "body": "test",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1545082650636",
                "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                "ApproximateFirstReceiveTimestamp": "1545082650649",
            },
            "messageAttributes": {},
            "md5OfBody": "098f6bcd4621d373cade4e832627b4f6",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
            "awsRegion": "us-east-2",
        },
    ]
}
