<template>
  <div>
    <h3>Alert!</h3>
    <p>
        Pathogen {{ pathogen }} detected in room {{ room }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'Alert',
  props: ['pathogen', 'room'],
};
</script>