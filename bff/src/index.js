const express = require("express");
const app = express();
const port = 1235;

app.use(express.static("../frontend/dist"));
app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
