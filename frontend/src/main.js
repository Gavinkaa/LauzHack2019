import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

const vue = new Vue({
  router,
  data: {
    connected: false,
  },
  render: h => h(App),
});

vue.$mount('#app');
