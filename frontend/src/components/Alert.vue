<template>
  <div>
    <div class="bg-white text-left border-red-500 border-2 rounded-lg p-4 mx-auto w-full md:w-1/2 lg:w-1/4 inline-block my-2 block shadow-lg">
      <h3 class="text-red-500 font-bold text-lg">Alert!</h3>
      <div>
        <span class="font-bold text-base">Pathogen:</span>
        <span class="text-base mx-2">{{ pathogen }}</span>
      </div>
      <div>
        <span class="font-bold text-base">Room:</span>
        <span class="text-base mx-2">{{ room }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Alert',
  props: ['pathogen', 'room'],
};
</script>