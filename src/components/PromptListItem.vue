<template>
    <li :id="id">{{ title }}</li>
</template>

<script>
export default {
    props: ['title', 'id']
}
</script>