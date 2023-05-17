<template>
  <div v-if="prompt" class="description-box">
    <h1 class="description-title">Description</h1>
    <p class="description-text">{{ prompt.description }}</p>
  </div>
  <p v-else>Loading</p>
  </template>

<script>
export default {
    props: ['prompt']
}
</script>