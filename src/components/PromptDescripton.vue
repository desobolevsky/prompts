<template>
    <div class="description-box">
      <div v-if="prompt">
        <h2>{{ prompt.title }}</h2>
        <p>{{ prompt.description }}</p>
      </div>
      <p v-else>Loading</p>
    </div>
  </template>

<script>
export default {
    props: ['prompt']
}
</script>