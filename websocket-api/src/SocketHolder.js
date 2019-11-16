const uuid = require('uuid/v4');

class SocketHolder {
  constructor() {
    this.hospitalSockets = new Map();
  }

  add(hospital, ws) {
    let sockets = this.hospitalSockets.get(hospital);
    if (!sockets) {
      sockets = new Map();
      this.hospitalSockets.set(hospital, sockets);
    }
    const client = uuid();
    sockets.set(client, ws);
    return client;
  }

  remove(hospital, client) {
    let sockets = this.hospitalSockets.get(hospital);
    if (sockets) {
      sockets.delete(client);
      if (sockets.size === 0) {
        this.hospitalSockets.delete(hospital);
      }
    }
  }

  sendToHospital(hospital, data) {
    const sockets = this.hospitalSockets.get(hospital);
    if (sockets) {
      for (const ws of sockets.values()) {
        ws.send(data);
      }
    }
    return 'Ok'
  }

  print() {
    const m = new Map();
    for (const [hospital, map] of this.hospitalSockets.entries()) {
      const m2 = new Map();
      m.set(hospital, m2);
      for (const [client, _] of map.entries()) {
        m2.set(client, 'WS');
      }
    }
    console.log(m);
  }
}

module.exports = SocketHolder;
