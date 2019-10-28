# cloud-events-handler
Send CloudEvents (and others) to a WSGI application

## Problem
How do handle events from your cloud provider of choice with your WSGI application?

_Events could be_
* [CloudEvents](https://cloudevents.io/)
* [AWS Events](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)
* Google, Azure events too

**Examples:**

```
CloudEvent -> Lambda that processes the data in the event
S3 event -> Lambda that processes the file added
EventBridge -> Lambda that processes the data in the event
```

#### Why would you want to do this?

A whole application has parts that are accessible via HTTP and some that are reactive to non-HTTP events.
The latter kind of event may need to be handled or processed with components from your application, e.g. middleware, models, serializers, etc.

## Install

```
pip install cloud-events
```

## Usage

[Example Django Application](./examples/example-django)

*AWS S3 Example*

1. Include `cloud-events` in the requirements
2. Set the handler of a lambda to `cloud_events.handler.handler`
3. Set `WSGI_APPLICATION` to the python path of the WSGI application
4. Process the S3 event at `/aws.s3` of your application


### Example

```
my-django-app
  views
    Books
```

```
GET /books  - returns a list of books

POST /books - possible but what if the book is > 6 MB? Lambda cannot handle that.
So let us allow users to upload that book directly to S3.
Now how do we get the metadata in the database when the user uploads the book?
We configure an event for each S3 object creation in our bucket.
Therefore, when the S3 event is sent, we want our Lambda to have access to the same code that the rest of our application uses.

DELETE /books/{id} - deletes a book
```

In this example instead of reacting only to an API Gateway or ALB event, we can process any event in our WSGI application.

### Settings

Two settings are used to configure the cloud-event handler.

**Required** `WSGI_APPLICATION` points to the python path of the WSGI application.

*Optional* `WSGI_ENVIRON` points to the python path of a module and is expected to end at a dictionary.

Example `WSGI_ENVIRON`

```
# in app/config
environ = {
    "HTTP_ACCEPT": "application/vnd.api+json",
    "PATH_INFO": "/books/",
    "REQUEST_METHOD": "get"
}

WSGI_ENVIRON = app.config.environ
```

This is merged with the default environ and passed to the WSGI application.

Default environ:

```
{
    "CONTENT_TYPE": "application/json",
    "REQUEST_METHOD": "post",
    "PATH_INFO": "/",
    "SCRIPT_NAME": "",
    "SERVER_NAME": "localhost",
    "SERVER_PORT": "80",
    "SERVER_PROTOCOL": str("HTTP/1.1"),
    "wsgi.input": None,
    "wsgi.version": (1, 0),
    "wsgi.run_once": False,
    "wsgi.multiprocess": False,
    "wsgi.multithread": False,
    "wsgi.url_scheme": "http",
}
```

### Custom Handler

You can use a custom handler instead of the provided handler by importing the handler function and passing the `event` and `context` .

```
from cloud_events.handler import handler

def my_handler(event, context):
    do_my_special_thing()
    return handler(event, context)
```

The default handler returns a dictionary.

```
{
    "status_code": response.status_code,
    "body": response.get_data(as_text=True),
    "headers": dict(response.headers),
}
```


## Event Path Mapping

| Event            | Path Attribute                                      | Dynamic WSGI Path |
| ---------------- | --------------------------------------------------- | ---------------- |
| CloudEvent       | `$.source`                                          | `/myContext`     |
| AWS EventBridge  | `$.source`                                          | `/com.my.event`   |
| AWS CloudWatch Event | `$.source`                                          | `/com.my.event`   |
| AWS IOT Event    | `$.event.eventName`                                 | `/myChargedEvent`        |

Events with a dynamic WSGI path mean that the path called in the WSGI application is dependent on the data in the event message at the path attribute specified.

| AWS Event        | Pattern Attributes                               | Static WSGI Path        |
| ---------------- | --------------------------------------------------- | ---------------- |
| S3           | `$.Records[0].eventSource` with `:` replaced by `.` | `/aws.s3`         |
| CodeCommit   | `$.Records[0].eventSource`                          | `/aws.codecommit` |
| DynamoDB         | `$.Records[0].eventSource`                          | `/aws.dynamodb`   |
| EC2 Lifecycle    | `$.source`                                          | `/aws.ec2`        |
| Kinesis          | `$.Records[0].eventSource` with `:` replaced by `.` | `/aws.kinesis`    |
| SNS              | `$.Records[0].eventSource` with `:` replaced by `.` | `/aws.sns`        |
| SQS              | `$.Records[0].eventSource` with `:` replaced by `.` | `/aws.sqs`        |
| SES              | `$.Records[0].eventSource` with `:` replaced by `.` | `/aws.ses`        |
| Lex              | `$.bot` and `$.outputDialogMode` and `$.currentIntent` | `/aws.lex`        |
| Kinesis Firehose | `$.records[0].kinesisRecordMetadata` | `/aws.kinesis.firehose`        |
| Cognito          | `$.identityId` and `$.identityPoolId` | `/aws.cognito`        |
| Config           | `$.configRuleId` | `/aws.config`        |
| CloudFront       | `$.Records[0].cf`                          | `/aws.cloudfront`   |
| CloudFormation   | `$.LogicalResourceId`                          | `/aws.cloudformation`   |
| Alexa   | `$.header` and `$.payload`                          | `/aws.alexa`   |

Events with a static WSGI path mean that the path called in the WSGI application is the same for each event matching the pattern. Some events are _essentially_ static since the route is defined by the message but that data is from AWS and unlikely to change.


## Getting Started

1. Clone this repo
2. Install tox `pip install tox`
3. Run tests `tox`

All package code is in `src`

## Frequently Asked Questions

Does this have ASGI support?

> No. It could be that was not the immediate need since ASGI is only supported in Django 3.0 and it turns off access to the database.

Is the responses JSON serializable?

> Yes. This is also to support SQS which needs a response from a lambda. The response code from the WSGI application is sent back in the default response i.e. a 500 in the WSGI app will then be sent to SQS if using the default handler.

Does this have API Gateway/ALB support?

> No. For now use other libraries as those are more fully featured.
>
> For AWS ALB and API Gateway events use [serverless-wsgi](https://github.com/logandk/serverless-wsgi), [zappa](https://github.com/Miserlou/Zappa), [awsgi](https://github.com/slank/awsgi) something else

Does this encourage monolithic lambdas?

> Maybe

#### History

This started out with the question, "Can we take an AWS event, in a generic way, and send it through to Django via a handler that makes full use of Django?"

> Yes we can :)


## Flow

```

                     +------------------+
                     |                  |
                     |  Event Producer  |
                     |                  |
                     +------------------+
                               |
                               |
         +---------------------v---------------------+
         |                                           |
         |              Event Consumer               |
         |                                           |
         |          +---------------------+          |
         |          |Handler              |          |
         |          |                     |          |
         |          |Any compute that     |          |
         |          |handles/processes the|          |
         |          |event                |          |
         |          +---------------------+          |
         |                     |                     |
         |                     v                     |
         |          +---------------------+          |
         |          |Adapter              |          |
         |          |                     |          |
         |          |Adapts events into   |          |
         |          |CloudEvents format   |          |
         |          +---------------------+          |
         |                     |                     |
         |                     v                     |
         |          +---------------------+          |
         |          |Interface            |          |
         |          |                     |          |
         |          |Interfaces for WSGI  |          |
         |          +---------------------+          |
         |                     |                     |
         |                     v                     |
         |          +---------------------+          |
         |          |Application          |          |
         |          |                     |          |
         |          |Any WSGI application |          |
         |          +---------------------+          |
         |                                           |
         +-------------------------------------------+

```
