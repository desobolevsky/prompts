<template>
  <a>Selected Prompt Id: {{ selectedPromptId }}</a>
  <PromptsList :prompts="prompts" :selectedPromptId="selectedPromptId" @selectPrompt="selectPrompt"/>
</template>

<script>
import { PROMPTS_API_LIST_PROMPTS_URL } from './settings';
import PromptsList from './components/PromptsList.vue'

const axios = require('axios');

export default {
  components: {
    PromptsList
  },
  data() {
    return {
      prompts: [],
      selectedPromptId: null,
    }
  },
  created(){
    axios.get(PROMPTS_API_LIST_PROMPTS_URL)
      .then(response => {
        (this.prompts = response.data)
      })
      .catch(error => {
        console.error(error)
      });
  },
  methods: {
    selectPrompt(promptId){
      this.selectedPromptId = promptId;
    }
  }
}
</script>