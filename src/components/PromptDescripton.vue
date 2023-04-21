<template>
  <div v-if="prompt" class="description-box">
    <p>{{ prompt.description }}</p>
  </div>
  <p v-else>Loading</p>
  </template>

<script>
export default {
    props: ['prompt']
}
</script>