<template>
    <div class="template-wrapper">
        <span class="template-hint">template</span>
        <h2 class="template-text">{{ promptTemplate }}</h2>
    </div>
</template>

<script>
export default {
  props: ['promptTemplate']
}
</script>