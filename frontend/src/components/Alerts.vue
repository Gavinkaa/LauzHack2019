<template>
  <div class="text-center">
    <Alert
      v-for="({pathogen, room},index) in alerts"
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
};
</script>