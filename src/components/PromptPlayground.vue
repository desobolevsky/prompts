<template>
    <div class="playground-box">
      <p v-if="prompt">Content: {{ prompt.content }}</p>
      <p v-else>Loading</p>
    </div>
  </template>

<script>
export default {
    props: ['prompt']
}
</script>