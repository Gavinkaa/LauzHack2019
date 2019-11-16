<template>
  <div id="app">
    <Alert v-for="{pathogen, item} of alerts" :key="pathogen" :pathogen="pathogen" :item="item" />
    <div>
      <h3>Pathogen:</h3>
      <input v-model="pathogen" />
    </div>
    <div>
      <h3>Room:</h3>
      <input v-model="room" />
    </div>
    <button v-on:click="create">Create</button>
    <button v-on:click="connect">Connect</button>
  </div>
</template>

<script>
import Alert from './components/Alert';
import { connect } from './socket';

export default {
  name: 'app',
  components: {
    Alert,
  },
  data() {
    return { pathogen: '', room: '', alerts: [] };
  },
  methods: {
    create() {
      this.alerts.push({ pathogen: this.pathogen, room: this.room });
    },

    connect() {
      connect();
    }
  },
};
</script>

<style>
</style>
