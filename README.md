# django-channels-demo
A proof-of-concept project using Django channels with some load testing experiments using Tsung.

## Usage
Run `make runserver` to get going fast.

Connect to `localhost:8000`. The page display a "Dynamic Articles" view. Upon connection, the latest 5 artciles are sent using a websocket. Whenever an article is added via the admin interface (`localhost:8000/admin`) thereafter, it is automatically pushed to all connected websockets.

To fire up a load test, run `make tsung`.

## Quick overview

When visiting the root page, a websocket is created and added to a channel `Group`, which is a list of current `subscribers`.

Django signals are used to catch `Article` creation events. The event handler sends a message to the subscriber group.

The `Article` models are serialised using Django's built-in JSON serialiser.

## Things to note
* Delivery is not guarenteed and I have seen messages going missing under (minor) load. Ref: http://channels.readthedocs.io/en/stable/faqs.html#why-isn-t-there-guaranteed-delivery-a-retry-mechanism
* The `websocketbridge.js` library bundled with `channels` has a reconnect retry strategy. This is now used.
* When configuring the `channel_capacity` it is important to set a value for `daphne.response*`. This was not clear in the documentation.
* Redis gets polluted with keys that are never (from what I observed) removed (e.g. `asgi-meta:daphne.response.ckLvSTDSRG!:messages_count`. These may be due to errors occurring, but it is an operational aspect to keep in mind.



## TODO
* Tests using [ChannelTestCase](http://channels.readthedocs.io/en/stable/testing.html#channeltestcase)
* Investigate handling of https://github.com/django/daphne/issues/63 (Request Queue Full), which affects both the HTTP and websocket requests. (Done...this was related to the `daphne.response` channel size.)
* `asgi_redis` [config](https://github.com/django/asgi_redis/#usage)
* Note that the Tsung tests currently do not work via `nginx`.

