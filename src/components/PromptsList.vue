<template>
    <PromptListItem
      v-for="prompt in prompts"
      :key="prompt.id"
      :title="prompt.title"
      :id="prompt.id"
       />
</template>

<script>
import PromptListItem from './PromptListItem.vue';

export default {
    components: {
        PromptListItem
    },
    props: ['prompts']
}
</script>