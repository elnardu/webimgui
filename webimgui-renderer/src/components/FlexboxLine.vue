<template>
  <div class="flexbox-line">
    <LayoutElement v-for="(child, i) in children" :key="i" :layout="child" />
  </div>
</template>

<script>
import LayoutElement from "./LayoutElement.js";

export default {
  props: ["meta", "children"],
  components: {
    LayoutElement
  }
};
</script>

<style scoped>
.flexbox-line {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  flex-wrap: wrap;
  margin-bottom: calc(0.5rem - 0.125rem);
}
.flexbox-line > * {
  margin-right: 0.25rem !important;
  margin-top: 0.125rem !important;
  margin-bottom: 0.125rem !important;
}
</style>
