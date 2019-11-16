const app = require('express')();
require('express-ws')(app);
const port = 1234;

app.ws('/join', (ws, req) => {
  ws.on('message', msg => {
    ws.send(msg);
  });
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
