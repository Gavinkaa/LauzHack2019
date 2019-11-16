export function connect() {
  const socket = new WebSocket("ws://localhost:1234");
  socket.addEventListener("open", () => {
    console.log("connected!");
    socket.send("Hello!");
  });
  socket.addEventListener("message", event => {
    console.log(event.data);
  });
}
