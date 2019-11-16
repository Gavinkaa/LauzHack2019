# API

## Create a new event

This will tell this service to create a new alert for a given hospital, warning about a specific
pathogen in a room.

`data.json`:

```
{
  "hospital": "BC",
  "samples": [
    { "pathogen": "AABBBB", "hospital": "BC", "room": "BC020" },
    { "pathogen": "BBAAA", "hospital": "BC", "room": "BC021" }
  ]
}
```

```
http POST /alert < data.json
```

## Websocket API

### Connect to the Websocket

```
websocat ws://this/join?hospital=BC
```

### Events

We use websockets, so events look like this:

```
{type: 'alert', {pathogen: 'Evil', room: 'BC010'}};
```
