<template>
  <div id="app" class="h-screen m-0 bg-gray-200 p-12">
    <div v-if="!connection" class="bg-white rounded-lg w-full md:w-1/2 lg:w-1/4 p-8 shadow-lg">
      <h3 class="text-2xl font-bold">Hospital Name:</h3>
      <div class="h-1/2">
        <input class="h-full text-base p-2 my-4 border rounded shadow" v-model="hospital" />
      </div>
      <button
        class="bg-blue-500 hover:bg-blue-700 text-base text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        v-on:click="connect"
      >Connect</button>
    </div>
    <div class="text-center">
      <Alert v-for="{pathogen, room} of alerts" :key="pathogen" :pathogen="pathogen" :room="room" />
    </div>
  </div>
</template>

<script>
import Alert from './components/Alert';
import Connection from './Connection';

export default {
  name: 'App',
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

<style src="./assets/css/tailwind.css">
</style>
