<template>
  <div class="columns">
    <LayoutElement v-for="(child, i) in children" :key="i" :layout="child" />
  </div>
</template>

<script>
import LayoutElement from "./LayoutElement.js";

export default {
  props: ["children"],
  components: {
    LayoutElement
  }
};
</script>

