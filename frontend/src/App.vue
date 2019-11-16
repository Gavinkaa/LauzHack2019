<template>
  <div id="app">
    <div>{{ message }}</div>
    <div>
      <input v-model="message" />
    </div>
    <h>Reversed</h>
    <div>{{ reverseMessage }}</div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return { message: 'Hello!' };
  },
  computed: {
    reverseMessage() {
      return this.message + 'Lol';
    }
  }
};
</script>

<style>
</style>
