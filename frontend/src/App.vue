<template>
  <div>
    <div v-if="$router.currentRoute.name !== 'Login'">
      <div class="bg-blue-600 text-white p-4">
        <nav class="">
          <router-link class="px-10 uppercase text-xl font-semibold" to="/alerts">Alerts</router-link>
          <router-link class="px-10 uppercase text-xl font-semibold" to="/maps">Maps</router-link>
        </nav>
      </div>
    </div>

    <div id="app" class="h-screen bg-gray-200 p-12">
      <router-view v-on:join="newHospital" v-bind:alerts="alerts"></router-view>
    </div>
  </div>
</template>

<script>
import Connection from './Connection';

export default {
  name: 'App',
  data() {
    return { connection: undefined, alerts: [], i: 0 };
  },
  methods: {
    newHospital(hospital) {
      this.$root.connected = true;
      this.connection = new Connection(hospital);
      this.connection.onAlert(details => {
        this.i += 1;
        this.alerts = this.alerts.filter(a => a.pathogen !== details.pathogen && a.room !== details.room);
        this.alerts.unshift({...details, i: this.i })
      });
      this.$router.push({ path: '/alerts' });
    },
  },
};
</script>

<style src="./assets/css/tailwind.css">
</style>
