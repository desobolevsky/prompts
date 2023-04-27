<template>
  <div v-if="prompt" class="playground-box">
    <div class="title-box">
      <h1 class="title">{{ prompt.title }}</h1>
    </div>
    <div class="template-box">
      <div class="template-wrapper">
        <span class="template-hint">template</span>
        <h2 class="template-text">{{ prompt.template }}</h2>
      </div>
    </div>

    <div class="examples-box">
      <div v-for="(example, index) in prompt.examples" :key="index" class="example-box">
        <div class="example-content">
          <div class="message-box-user">
            <div class="message-part">
              <img :src="require('@/assets/user-icon.png')" alt="User avatar">
            </div>
            <div class="message-part message-text">
              <p>{{ example.user }}</p>
            </div>
          </div>
          <div class="message-box-chatgpt">
            <div class="message-part">
              <img :src="require('@/assets/chatgpt-icon.svg')" alt="ChatGPT avatar">
            </div>
            <div class="message-part message-text">
              <p>{{ example.system }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <p v-else>Loading</p>
</template>

<script>
export default {
  props: ['prompt']
}
</script>