<template>
  <a>Selected Prompt Id: {{ selectedPromptId }}</a>
  <PromptsList :selectedPromptId="selectedPromptId" @selectPrompt="selectPrompt"/>
</template>

<script>
import PromptsList from './components/PromptsList.vue'

export default {
  components: {
    PromptsList
  },
  data() {
    return {
      selectedPromptId: null,
    }
  },
  methods: {
    selectPrompt(promptId){
      this.selectedPromptId = promptId;
    }
  }
}
</script>