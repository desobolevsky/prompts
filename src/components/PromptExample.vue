<template>
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
</template>

<script>
export default {
  props: ['example']
}
</script>``