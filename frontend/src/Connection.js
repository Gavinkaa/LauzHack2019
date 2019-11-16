class Connection {
  constructor(hospital) {
    const socket = new WebSocket(
      `ws://localhost:1234/join?hospital=${hospital}`,
    );
    socket.addEventListener('message', event => {
      const json = JSON.parse(event.data);
      if (json.type === 'alert') {
        this.alert(json.details);
      }
    });
  }

  onAlert(cb) {
    this.alert = cb;
  }
}
export default Connection;
