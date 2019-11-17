<template>
  <div class="text-center">
    <div class="text-lg lg:text-xl bg-white rounded-lg mb-4 w-3/4 lg:w-1/2 shadow mx-auto p-4">
      <div class="text-align-bottom">
        <div class="uppercase font-bold">Filter by:</div>
        <dropdown
          :options="filterlist"
          :selected="typeselect"
          v-on:updateOption="methodToRunOnSelect"
        ></dropdown>
      </div>
      <div class="w-1/2 mx-auto my-2">
        <autocomplete :search="search" placeholder="input" @submit="handleSubmit"></autocomplete>
      </div>
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
import dropdown from 'vue-dropdowns';
import Autocomplete from '@trevoreyre/autocomplete-vue';

export default {
  name: 'Alerts',
  components: {
    Alert,
    Autocomplete,
    dropdown: dropdown,
  },
  props: ['alerts'],
  data() {
    return {
      select: undefined,
      filterlist: [{ name: 'room' }, { name: 'pathogen' }],
      typeselect: {
        name: 'Choose a filter',
      },
    };
  },
  methods: {
    methodToRunOnSelect(payload) {
      this.typeselect = payload;
    },
    search(input) {
      if (input.length < 1) {
        return [];
      }
      return this.alerts
        .map(x => (this.typeselect.name === 'room' ? x.room : x.pathogen))
        .filter(alert => {
          return alert.toLowerCase().startsWith(input.toLowerCase());
        });
    },
    handleSubmit(result) {
      this.select = result;
    },
  },
  computed: {
    filtered() {
      return this.alerts.filter(x => {
        const lowered = this.typeselect['name'].toLowerCase();
        if (lowered === 'room') {
          return (
            !this.select || x.room.toLowerCase() === this.select.toLowerCase()
          );
        } else if (lowered === 'pathogen') {
          return (
            !this.select ||
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