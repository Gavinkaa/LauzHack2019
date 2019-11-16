<template>
  <div id="app" class="h-screen bg-gray-200 p-12">
    <div v-if="$router.currentRoute.name !== 'Login'">
      <h2>Nav Bar</h2>
      <nav>
        <router-link to="/alerts">Alert Vue</router-link>
        <router-link to="/maps">Maps</router-link>
        <router-link to="/rooms">Rooms</router-link>
      </nav>
    </div>
    <router-view v-on:join="newHospital" v-bind:alerts="alerts"></router-view>
  </div>
</template>

<script>
import Connection from './Connection';

export default {
  name: 'App',
  data() {
    return { connection: undefined, alerts: [] };
  },
  methods: {
    newHospital(hospital) {
      this.$root.connected = true;
      this.connection = new Connection(hospital);
      this.connection.onAlert(details => this.alerts.push(details));
      this.$router.push({ path: '/alerts' });
    },
  },
};
</script>

<style src="./assets/css/tailwind.css">
</style>
