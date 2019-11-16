# API

## Create a new event

This will tell this service to create a new alert for a given hospital, warning about a specific
pathogen in a room.

```
http POST /alert pathogen=Evil room=BC010 hospital=BC
```

## Websocket API

### Connect to the Websocket

```
websocat ws://this/connect?hospital=BC
```

### Events

We use socket.io, so events look like this:
```
socket.on('alert', {pathogen: 'Evil', room: 'BC010'});
```
