<template>
  <p>
    {{meta.text}}
  </p>
</template>

<script>
  export default {
    props: ['meta']
  }
</script>

<style scoped>
p {
  margin-bottom: 0.5rem;
}
</style>
