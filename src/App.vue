<template>
  <PromptsList :prompts="prompts"/>
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
      prompts: []
    }
  },
  created(){
    axios
      .get(PROMPTS_API_LIST_PROMPTS_URL)
      .then(response => (this.prompts = response.data));
  },
  methods: {}
}
</script>