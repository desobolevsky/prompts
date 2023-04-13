<template>
    <PromptListItem
      v-for="prompt in prompts"
      :key="prompt.id"
      :title="prompt.title"
      :id="prompt.id"
      :isSelected="selectedPromptId === prompt.id"
      @click="selectPrompt(prompt.id)"
       />
</template>

<script>
import PromptListItem from './PromptListItem.vue';
import { PROMPTS_API_LIST_PROMPTS_URL } from '../settings';

const axios = require('axios');

export default {
    
    data(){
        return {
            prompts: [],
        }
    },
    components: {
        PromptListItem
    },
    props: ['selectedPromptId'],
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
            this.$emit('selectPrompt', promptId);
        }
    }
}
</script>