<template>
  <div v-if="prompt" class="playground-box">
    <div class="title-box">
      <h1 class="title">{{ prompt.title }}</h1>
    </div>

    <div class="template-box">
      <PromptTemplate :prompt="prompt"/>
    </div>

    <div class="examples-box">
      <PromptExample
        v-for="(example, index) in prompt.examples"
        :key="index"
        :example="example"
      />
    </div>
  </div>

  <p v-else>Loading</p>
</template>

<script>
import PromptExample from './PromptExample.vue';
import PromptTemplate from './PromptTemplate.vue';

export default {
  props: ['prompt'],
  components: {
    PromptExample,
    PromptTemplate
  }
}
</script>