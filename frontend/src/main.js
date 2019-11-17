import Vue from 'vue';
import VueKonva from 'vue-konva';
import App from './App.vue';
import router from './router';
import Autocomplete from '@trevoreyre/autocomplete-vue';
import '@trevoreyre/autocomplete-vue/dist/style.css';

Vue.config.productionTip = false;
Vue.use(Autocomplete);
Vue.use(VueKonva);

const vue = new Vue({
  router,
  data: {
    connected: false,
  },
  render: h => h(App),
});

vue.$mount('#app');
