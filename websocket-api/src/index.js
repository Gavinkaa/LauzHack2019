const app = require('express')();
require('express-ws')(app);
const bodyparser = require('body-parser');
const SocketHolder = require('./SocketHolder.js');

app.use(bodyparser.json());

const port = 1234;

const holder = new SocketHolder();

app.post('/alert', (req, res) => {
  console.log(req.body);
  const { hospital, samples } = req.body;
  for (const { pathogen, room } of samples) {
    const data = JSON.stringify({ type: 'alert', details: { pathogen, room } });
    holder.sendToHospital(hospital, data);
  }
  res.send('OK');
});

app.ws('/join', (ws, req) => {
  const hospital = req.query.hospital;
  const client = holder.add(hospital, ws);
  console.log('join', hospital, client);
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
