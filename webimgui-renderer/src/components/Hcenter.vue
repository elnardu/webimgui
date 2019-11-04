<template>
  <div class="hcenter">
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

<style>
.hcenter {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style>

