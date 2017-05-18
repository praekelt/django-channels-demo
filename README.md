# django-channels-demo
A proof-of-concept project using Django channels

## Usage
Run `make runserver` to get going fast.

Connect to `localhost:8000`. The page display a "Dynamic Articles" view. Upon connection, the latest 5 artciles are sent using a websocket. Whenever an article is added via the admin interface (`localhost:8000/admin`) thereafter, it is automatically pushed to all connected websockets.

## Quick overview

When visiting the root page, a websocket is created and added to a channel `Group`, which is a list of current `subscribers`.

Django signals are used to catch `Article` creation events. The event handler sends a message to the subscriber group.

The `Article` models are serialised using Django's built-in JSON serialiser.

## Things to note
* Delivery is not guarenteed and I have seen messages going missing under (minor) load. Ref: http://channels.readthedocs.io/en/stable/faqs.html#why-isn-t-there-guaranteed-delivery-a-retry-mechanism
* The `websocketbridge.js` library bundled with `channels` has a reconnect retry strategy. This is now used.

## TODO
* Webscoket ping-pong
* Tests using [ChannelTestCase](http://channels.readthedocs.io/en/stable/testing.html#channeltestcase)
* Investigate handling of https://github.com/django/daphne/issues/63 (Request Queue Full), which affects both the HTTP and websocket requests.
* `asgi_redis` [config](https://github.com/django/asgi_redis/#usage)


