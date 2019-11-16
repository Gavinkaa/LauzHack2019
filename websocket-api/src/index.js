const app = require('express')();
require('express-ws')(app);
const port = 1234;

const hospitalSockets = new Map();

app.ws('/join', (ws, req) => {
  const hospital = req.query.hospital;
  console.log(`Adding hospital ${hospital}`);
  hospitalSockets.set(hospital, ws);
  ws.on('close', msg => {
    console.log(`Removing hosptial ${hospital}`);
    hospitalSockets.delete(hospital);
  });
  ws.on('message', msg => {
    ws.send(msg);
  });
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
