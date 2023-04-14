<template>
  <a>Selected Prompt Id: {{ selectedPromptId }}</a>
  <div class="container">
    <div class="left-part">
      <PromptsList :selectedPromptId="selectedPromptId" @selectPrompt="selectPrompt" />
    </div>
    <div class="central-part">
      <PromptPlayground :prompt="prompt" />
    </div>
    <div class="right-part">
      <PromptDescripton :prompt="prompt" />
      <CopyPromptButton :prompt="prompt" />
    </div>
  </div>
</template>

<script>
import CopyPromptButton from './components/CopyPromptButton.vue';
import PromptsList from './components/PromptsList.vue';
import PromptDescripton from './components/PromptDescripton.vue';
import PromptPlayground from './components/PromptPlayground.vue';
import { PROMPTS_API_LIST_PROMPTS_URL } from './settings';

const axios = require('axios');

export default {
  components: {
    CopyPromptButton,
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