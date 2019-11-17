<template>
  <div class="text-center">
    <div class="text-lg lg:text-xl bg-white rounded-lg mb-4 w-full lg:w-1/2 shadow mx-auto p-4">
      <span class="uppercase font-bold">Filter by:</span>
      <input class="px-2 mx-2 rounded border shadow" v-model="typeselect" />
      <input class="px-2 mx-2 rounded border shadow" v-model="select" />
      <autocomplete :search="search" placeholder="input"></autocomplete>
    </div>
    <Alert
      v-for="({pathogen, room}, index) in filtered"
      :key="index"
      :pathogen="pathogen"
      :room="room"
    />
  </div>
</template>



<script>
import Alert from './Alert';
import Autocomplete from '@trevoreyre/autocomplete-vue';

export default {
  name: 'Alerts',
  components: {
    Alert,
    Autocomplete,
  },
  props: ['alerts'],
  data() {
    return { select: '', typeselect: '' };
  },
  methods: {
    search(input) {
      if (input.length < 1) {
        return [];
      }
      return this.alerts
        .map(x => x.room)
        .filter(alert => {
          console.log(alert);
          return alert.toLowerCase().startsWith(input.toLowerCase());
        });
    },
  },
  computed: {
    filtered() {
      return this.alerts.filter(x => {
        const lowered = this.typeselect.toLowerCase();
        if (lowered === 'room') {
          return (
            this.select === '' ||
            x.room.toLowerCase() === this.select.toLowerCase()
          );
        } else if (lowered === 'pathogen') {
          return (
            this.select === '' ||
            x.pathogen.toLowerCase() === this.select.toLowerCase()
          );
        } else {
          return true;
        }
      });
    },
  },
};
</script>