<template>
  <div class="field">
    <label class="label">{{ text }}</label>
    <b-slider
      :value="$store.state.interactiveElementsState[meta.label]"
      :min="meta.min"
      :max="meta.max"
      :step="meta.step"
      @change="change"
    ></b-slider>
  </div>
</template>

<script>
import { labelToText } from "@/helpers";

export default {
  props: ["meta"],
  methods: {
    change(number) {
      this.$store.dispatch("submitAction", {
        label: this.meta.label,
        data: number
      });
    }
  },
  computed: {
    text() {
      return labelToText(this.meta.label);
    }
  }
};
</script>

<style scoped>
.select {
  margin-bottom: 0.5rem;
}
</style>
