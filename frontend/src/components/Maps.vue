<template>
  <div>
    <v-stage :config="configKonva">
      <v-layer>
        <v-image :config="configBC"></v-image>
      </v-layer>
      <v-layer>
        <v-image v-for="virus of liveViruses" :key="virus.room" :config="virus"></v-image>
      </v-layer>
    </v-stage>
  </div>
</template>

<script>
import virus from '../assets/virus.png';
import logo from '../assets/logo.png';
import bc from '../assets/BC.png';

export default {
  name: 'Maps',
  props: ['alerts'],
  data() {
    const rooms = [
      { room: 'BC01', x: 345, y: 10 },
      { room: 'BC02', x: 326, y: 178 },
      { room: 'BC03', x: 334, y: 280 },
      { room: 'BC04', x: 326, y: 408 },
      { room: 'BC05', x: 100, y: 140 },
      { room: 'BC06', x: 100, y: 240 },
      { room: 'BC07', x: 100, y: 330 },
      { room: 'BC08', x: 100, y: 400 },
      { room: 'BC09', x: 106, y: 2 },
      { room: 'BC010', x: 50, y: 2 },
    ];
    const bcimage = new Image();
    bcimage.src = bc;
    return {
      configKonva: {
        width: 600,
        height: 600,
      },
      configBC: {
        x: 0,
        y: 0,
        width: 4 * 100,
        height: 4 * 153,
        image: bcimage,
      },
      viruses: rooms.map(({ room, x, y }) => {
        return {
          room,
          x,
          y,
          width: 40,
          height: 40,
          image: new Image(),
        };
      }),
    };
  },
  computed: {
    liveViruses() {
      return this.viruses.filter(v => this.alerts.findIndex(x => x.room === v.room) !== -1)
    }
  },
  mounted() {
    for (const v of this.viruses) {
      v.image.src = virus;
    }
  },
};
</script>