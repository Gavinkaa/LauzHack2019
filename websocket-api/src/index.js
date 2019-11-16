const app = require('express')();
require('express-ws')(app);
const bodyparser = require('body-parser');
const SocketHolder = require('./SocketHolder.js');

app.use(bodyparser.json());

const port = 1234;

const holder = new SocketHolder();

app.post('/alert', (req, res) => {
  const { pathogen, hospital, room } = req.body;
  const data = JSON.stringify({ type: 'alert', details: { pathogen, room } });
  const result = holder.sendToHospital(hospital, data);
  res.send(result);
});

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
