const app = require('express')();
require('express-ws')(app);
const SocketHolder = require('./SocketHolder.js');

const port = 1234;

const holder = new SocketHolder();

app.ws('/join', (ws, req) => {
  const hospital = req.query.hospital;
  const client = holder.add(hospital, ws);
  ws.on('close', msg => {
    holder.remove(hospital, client);
  });
  ws.on('message', msg => {
    ws.send(msg);
  });
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
