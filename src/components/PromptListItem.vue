<template>
    <li :class="{ 'selected': isSelected }" >{{ title }}</li>
</template>

<script>
export default {
    props: ['title', 'id', 'isSelected']
}
</script>

<style>
li.selected {
    font-weight: bold;
}
</style>