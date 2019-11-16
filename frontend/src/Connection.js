class Connection {
  constructor(hospital) {
    const socket = new WebSocket(
      `ws://localhost:1234/join?hospital=${hospital}`,
    );
    socket.addEventListener('open', () => {
      console.log('connected!');
    });
    socket.addEventListener('message', event => {
      const json = JSON.parse(event.data);
      console.log(json);
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
