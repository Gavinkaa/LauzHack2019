<template>
  <div id="app">
    <div v-if="!connection">
      <h3>Hospital:</h3>
      <input v-model="hospital" />
      <button v-on:click="connect">Connect</button>
    </div>
    <Alert v-for="{pathogen, item} of alerts" :key="pathogen" :pathogen="pathogen" :item="item" />
  </div>
</template>

<script>
import Alert from './components/Alert';
import Connection from './Connection';

export default {
  name: 'app',
  components: {
    Alert,
  },
  data() {
    return { connection: undefined, hospital: '', alerts: [] };
  },
  methods: {
    connect() {
      this.connection = new Connection(this.hospital);
      this.connection.onAlert(details => this.alerts.push(details));
    },
  },
};
</script>

<style>
</style>
