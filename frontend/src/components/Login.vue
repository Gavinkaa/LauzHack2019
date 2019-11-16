<template>
  <div class="bg-white rounded-lg w-full md:w-1/2 lg:w-1/4 p-8 shadow-lg">
    <h3 class="text-2xl font-bold">Hospital Name:</h3>
    <div class="h-1/2">
      <input class="h-full text-base p-2 my-4 border rounded shadow" v-model="hospital" />
    </div>
    <button
      class="bg-blue-500 hover:bg-blue-700 text-base text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      v-on:click="connect"
    >Connect</button>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return { hospital: '' };
  },
  methods: {
    connect() {
      this.$emit('join', this.hospital);
    },
  },
};
</script>