<template>  
  <div v-if="prompt">
    <h3>{{ prompt.template }}</h3>
    <div v-for="(example, index) in prompt.examples" :key="index">
      <p>User: {{ example.user }}</p>
      <p>ChatGPT: {{ example.system }}</p>
    </div>
  </div>
  <p v-else>Loading</p>
</template>

<script>
export default {
    props: ['prompt']
}
</script>