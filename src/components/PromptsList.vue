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

export default {
    components: {
        PromptListItem
    },
    props: ['prompts', 'selectedPromptId'],
    methods: {
        selectPrompt(promptId){
            this.$emit('selectPrompt', promptId);
        }
    }
}
</script>