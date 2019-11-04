<template>
  <div class="container is-fluid">
    <LayoutElement v-if="layout" :layout="layout" />
  </div>
</template>

<script>
import LayoutElement from "@/components/LayoutElement";

import { mapState } from "vuex";

export default {
  name: "home",
  components: { LayoutElement },
  computed: mapState(["layout"])
};
</script>

<style scoped>
.container {
  padding: 0.5rem;
}
</style>
