<template>
  <a>Selected Prompt Id: {{ selectedPromptId }}</a>
  <div class="container">
    <PromptsList :selectedPromptId="selectedPromptId" @selectPrompt="selectPrompt" />
    <PromptPlayground :prompt="prompt" />
    <PromptDescripton :prompt="prompt" />
  </div>
</template>

<script>
import PromptsList from './components/PromptsList.vue';
import PromptDescripton from './components/PromptDescripton.vue';
import PromptPlayground from './components/PromptPlayground.vue';
import { PROMPTS_API_LIST_PROMPTS_URL } from './settings';

const axios = require('axios');

export default {
  components: {
    PromptsList,
    PromptDescripton,
    PromptPlayground
  },
  data() {
    return {
      selectedPromptId: null,
      prompt: null,
    }
  },
  methods: {
    selectPrompt(promptId) {
      this.selectedPromptId = promptId;
      this.getPrompt(promptId);
    },
    getPrompt(promptId) {
      const getPromptUrl = `${PROMPTS_API_LIST_PROMPTS_URL}${promptId}`;
      axios.get(getPromptUrl)
        .then(response => {
          (this.prompt = response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
}
</script>

<style>
@import "@/assets/styles.css";
</style>