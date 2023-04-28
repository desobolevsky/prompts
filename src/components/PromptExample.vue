<template>
  <div class="example-box-wrapper">
    <div class="example-box">

      <div class="user-message-box">
        <div class="message-avatar">
          <img :src="require('@/assets/images/user-icon.png')" alt="User avatar">
        </div>
        <div class="message-text">
          <p>{{ example.user }}</p>
        </div>
      </div>

      <div class="chatgpt-message-box">
        <div class="message-avatar">
          <img :src="require('@/assets/images/chatgpt-icon.svg')" alt="ChatGPT avatar">
        </div>
        <div class="message-text">
          <p>{{ example.system }}</p>
        </div>
      
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['example']
}
</script>``