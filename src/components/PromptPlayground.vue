<template>  
  <p v-if="prompt">Content: {{ prompt.content }}</p>
  <p v-else>Loading</p>
</template>

<script>
export default {
    props: ['prompt']
}
</script>