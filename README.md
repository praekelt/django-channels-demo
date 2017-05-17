# django-channels-demo
A proof-of-concept project using Django channels

## Usage
Run `make runserver` to get going fast.

Connect to `localhost:8000`. The page display a "Dynamic Articles" view. Upon connection, the latest 5 artciles are sent using a websocket. Whenever an article is added via the admin interface (`localhost:8000/admin`) thereafter, it is automatically pushed to all connected websockets.

## Quick overview

When visiting the root page, a websocket is created and added to a channel `Group`, which is a list of current `subscribers`.

Django signals are used to catch `Article` creation events. The event handler sends a message to the subscriber group.

The `Article` models are serialised using Django's built-in JSON serialiser.


## TODO
* Webscoket ping-pong
* Reconnecting JavaSCript websockets: https://github.com/joewalnes/reconnecting-websocket

