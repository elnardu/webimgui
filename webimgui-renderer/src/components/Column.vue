<template>
  <div :class="style">
    <LayoutElement v-for="(child, i) in children" :key="i" :layout="child" />
  </div>
</template>

<script>
import LayoutElement from "./LayoutElement.js";

export default {
  props: ["children", "meta"],
  components: {
    LayoutElement
  },
  computed: {
    style() {
      if (this.meta.size) {
        return `column is-${this.meta.size}`
      } else {
        return "column"
      }
    }
  }
};
</script>

