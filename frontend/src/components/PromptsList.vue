<template>
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
              this.prompts = response.data;
              const defaultSelectedPromptId = this.getDefaultSelectedPromptId();
              this.selectPrompt(defaultSelectedPromptId);
          })
          .catch(error => {
              console.error(error)
          });
    },
    methods: {
        selectPrompt(promptId){
            this.$emit('selectPrompt', promptId);
            localStorage.setItem('lastSelectedPromptId', promptId);
        },
        getDefaultSelectedPromptId(){
            const lastSelectedPromptId = parseInt(localStorage.getItem('lastSelectedPromptId'));
            const promptsIds = this.prompts.map(prompt => prompt.id);
            if (!isNaN(lastSelectedPromptId) || promptsIds.includes(lastSelectedPromptId)){
                return lastSelectedPromptId;
            }
            return this.prompts[0].id ;
        }
    }
}
</script>