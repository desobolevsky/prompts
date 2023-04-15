<template>
    <button :disabled="!prompt" @click="copyPromptContentToClipboard">
        <p>{{ buttonText }}</p>
    </button>
</template>

<script>
const DEFAULT_BUTTON_TEXT = "🗒️ Copy"
const COPIED_BUTTON_TEXT = "✅ Copied!"
const COPIED_BUTTON_TEXT_TIMEOUT_MS = 3000;

export default {
  data(){
    return {
        "buttonText": DEFAULT_BUTTON_TEXT
    } 
  },
  props: ['prompt'],
  methods: {
    copyPromptContentToClipboard() {
      const promptContent = this.prompt.template;
      navigator.clipboard.writeText(promptContent).then(() => {
        this.buttonText = COPIED_BUTTON_TEXT;
        setTimeout(() => {
            this.buttonText = DEFAULT_BUTTON_TEXT;
        }, COPIED_BUTTON_TEXT_TIMEOUT_MS);
      }, () => {
        console.error('Failed to copy to clipboard: ', promptContent);
      });
    }
  }
};
</script>