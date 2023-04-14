<template>
    <div class="list-box">
        <div v-if="prompts">
            <PromptListItem
                v-for="prompt in prompts"
                :key="prompt.id"
                :title="prompt.title"
                :id="prompt.id"
                :isSelected="selectedPromptId === prompt.id"
                @click="selectPrompt(prompt.id)"
            />
        </div>
        <p v-else>Loading</p>
    </div>
</template>

<script>
import PromptListItem from './PromptListItem.vue';
import { PROMPTS_API_LIST_PROMPTS_URL } from '../settings';

const axios = require('axios');

export default {
    
    data(){
        return {
            prompts: null,
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