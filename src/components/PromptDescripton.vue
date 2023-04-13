<template>
    <div>
      <h2>{{ prompt.title }}</h2>
      <p>{{ prompt.description }}</p>
    </div>
  </template>

<script>
export default {
    props: ['prompt']
}
</script>