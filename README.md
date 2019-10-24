# cloud-events-handler
Send CloudEvents (and AWS Events) to a WSGI application

## Example Problem
How do we use Django (or any WSGI compatible framework) to handle events?

_Events could be_
* CloudEvents from CNCF - https://cloudevents.io/
* AWS, Google, Azure events too

Django is tied to the web, really HTTP. CloudEvents are part of that but do not share the same expressions.

### Examples:
```
S3 event -> Lambda that processes the file added
EventBridge -> Lambda that processes the data in the event
```

Why would one want to do this?
A whole application has parts that are accessible via HTTP and some that are reactive to non-HTTP events.
The latter kind of event may need to be handled or processed with components from the Django application, e.g. middleware, models, serializers, etc.


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
Now how do we get the meta data in the database when the user uploads the book?
We configure an event for each S3 object creation in our bucket (configuring is outside the scope of this).
Therefore, when the S3 event is sent, we want our Lambda to have access to the same code that the rest of our application uses.

DELETE /books/{id} - deletes a book
```

So, can we take an AWS event, in a generic way, and send it through to Django via a handler that makes full use of Django?

I think so.

**This is a work in progress.**

## Flow
```



                     +------------------+
                     |                  |
                     |  Event Producer  |
                     |                  |
                     +------------------+
                               |
                               |
                               |
                               |
                               |
         +---------------------v---------------------+
         |                                           |
         |              Event Consumer               |
         |                                           |
         |                                           |
         |                                           |
         |                                           |
         |          +---------------------+          |
         |          |Handler              |          |
         |          |                     |          |
         |          |Any compute that     |          |
         |          |handles/processes the|          |
         |          |event                |          |
         |          |                     |          |
         |          +---------------------+          |
         |                     |                     |
         |                     v                     |
         |          +---------------------+          |
         |          |Adapter              |          |
         |          |                     |          |
         |          |Adapts events into   |          |
         |          |CloudEvents format   |          |
         |          |                     |          |
         |          +---------------------+          |
         |                     |                     |
         |                     |                     |
         |                     v                     |
         |          +---------------------+          |
         |          |Interface            |          |
         |          |                     |          |
         |          |Interfaces for WSGI  |          |
         |          |                     |          |
         |          +---------------------+          |
         |                     |                     |
         |                     |                     |
         |                     v                     |
         |          +---------------------+          |
         |          |Application          |          |
         |          |                     |          |
         |          |Any WSGI application |          |
         |          |                     |          |
         |          +---------------------+          |
         |                                           |
         |                                           |
         +-------------------------------------------+


```
