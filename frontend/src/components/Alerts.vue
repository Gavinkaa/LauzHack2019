<template>
  <div class="text-center">
    <div class="text-lg lg:text-xl bg-white rounded-lg mb-4 w-full lg:w-1/2 shadow mx-auto p-4">
      <span class="uppercase font-bold">Filter by:</span>
      <input class="px-2 mx-2 rounded border shadow" v-model="typeselect" />
      <input class="px-2 mx-2 rounded border shadow" v-model="select" />
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

export default {
  name: 'Alerts',
  components: { Alert },
  props: ['alerts'],
  data() {
    return { select: '', typeselect: '' };
  },
  computed: {
    filtered() {
      return this.alerts.filter(x => {
        const lowered = this.typeselect.toLowerCase();
        if (lowered === 'room') {
          return this.select === '' || x.room.toLowerCase() === this.select.toLowerCase();
        } else if (lowered === 'pathogen') {
          return this.select === '' || x.pathogen.toLowerCase() === this.select.toLowerCase();
        } else {
          return true;
        }
      });
    },
  },
};
</script>