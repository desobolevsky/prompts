<template>
    <div class="template-wrapper">
        <div>
          <span class="template-hint">template</span>
          <h2 class="template-text">{{ prompt.template }}</h2>
        </div>
        <CopyPromptButton :prompt="prompt" />
    </div>
</template>

<script>
import CopyPromptButton from './CopyPromptButton.vue';

export default {
  props: ['prompt'],
  components: {
    CopyPromptButton,
  }
}
</script>