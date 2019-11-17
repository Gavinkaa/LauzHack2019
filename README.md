We're submitting this project under the **Sophia** challenge.

## Building/Running

In order to build and run the application, a handful of services need to be started (on the same machines).

For testing the API, installing [httpie](https://httpie.org/) is pretty helpful.

For the node services, you need a decently up to date version of `node` and `npm`.

This builds the frontend files, and starts the BFF at `localhost:1235`

```
cd frontend
npm install
npm run build
cd ../bff
npm install
node src/index.js
```

This starts the websocket API at `localhost:1234`
```
cd websocket-api
npm install
node src/index.js
```

For the python services, you need `python3`, along with a few dependencies:
```
python3 -m pip install flask sqlite3
```

The two python services can be started as follows:

```
cd mock
python3 sophiaAnalysis.py
```

```
cd hopital_API
python3 hopitalAPI.py
```

Now that everything is up in running, we can visit the frontend by opening the following in a browser:
```
localhost:1235
```

In order to test the reception of new samples, sample data is included with the repository itself:
```
http POST localhost:5000/samples < hopital_API/samples.json
```

## Inspiration

Sophia's presentation about their use of genomics for data driven medicine was quite interesting, but at the same time very approachable. We realized that we had the skills to tackle the infrastructural aspects of the projects, leaving the genomics to the experts. Because of this, we were inspired to work on the UX and presentation of an application relying on simplifying assumptions in terms of what kind of genomic analysis was available to us.

## What it does

We provide an API for hospitals to submit data about genomic samples collected throughout their location. They provide us information about what samples they took where, and then we process that data. Assuming the existence of some external service that gives us a species classification for a genome sequence (which we implemented in a simplified way), we provide real time feedback on where pathogens are developing throughout the hospital.

## How we built it

The following is a diagram of the architecture:
![](https://raw.githubusercontent.com/Gavinkaa/LauzHack2019/master/image%20(2).png)

We based it on a microservice architecture of sorts, implemented mainly in Node.JS and Python. We assume that if the prototype is scaled, the mock Sophia API will be replaced with a more robust internal implementation. As for the services entirely under our control, we have the following:

- Hospital service
- Websocket API
- Backend For Frontend

The Hospital service is a workhorse of the application. It provides an API for hospitals to submit their located samples. This service relies on the mocked Sophia API in order to detect pathogens. Whenever we detect pathogens among the samples, we send an event along to the Websocket API. This service is implemented in Python using Flask.

The database for the hospital service was done with SQLite and a lot of SQL statements.

The Websocket API, in turn, figures out how to route all the events it receives among the various clients connecting from different hospitals. Clients will be using our frontend application, and will be connected to this API, which can provide real time alerts about emerging threats and their location throughout the hospital. This API is implemented in Node.JS using Express.

The Backend For Frontend exists solely to serve the files that make up the frontend, this is a simple Node.js service that service the minified files.

The frontend itself was made using Vue, and quite a bit of tailwind CSS for the nice ux.

## Challenges we ran into

One of the challenges was figuring out the necessary granularity to give different services, as well as finding a way to avoid having task blocking other members of the team. We also had a certain amount of imbalance in terms of knowledge, which lead to some tasks taking quite a bit longer than expected as team members wrestled with new bugs.

Another point we got stuck on for a while was finding a good way to visualize the pathogen map. Overlaying multiple images is simple in theory, but difficult to integrate with the component based API provided by HTML. We had to cycle through quite a few libraries before finding something that even worked. Even then, we encountered odd cross platform bugs, and had to resort to beautiful workarounds such as hidden images.

## What we learned

Learning how to use Flask and Node.JS to make web applications.

Divying up an application into a scaleable set of microservices.

Using Vue to make nice frontends, and integrating with websockets.

Becoming masters of SQL Fu.

## What's next for pathogenZ

Because of the microservice architecture, each of the services can be scaled individually as necessary. The first step in integrating this into an actual application would be to replace the mock Sophia API with an actual implementation building upon the existing expertise in that domain.

Another point that could be improved is providing some kind of messaging queue between the Hospital service and the websocket API. Using something like Kafka could also allow us to guarantee that a certain number of clients have consume the alerts before we get rid of the information. One weakness of the current project is that a client that isn't connected when an alert happens will miss the alert.

The hospital database could be sharded in some way (probably based on Hospital, especially because of potential privacy issues).
