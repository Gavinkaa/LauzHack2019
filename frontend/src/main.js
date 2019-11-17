import Vue from 'vue';
import App from './App.vue';
import router from './router';
import Autocomplete from '@trevoreyre/autocomplete-vue';
import VuePIXI from 'vue-pixi';
import '@trevoreyre/autocomplete-vue/dist/style.css';

Vue.config.productionTip = false;
Vue.use(Autocomplete);
Vue.use(VuePIXI);

const vue = new Vue({
  router,
  data: {
    connected: false,
  },
  render: h => h(App),
});

vue.$mount('#app');
