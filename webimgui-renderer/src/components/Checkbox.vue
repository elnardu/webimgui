<template>
  <label class="checkbox">
    <input
      type="checkbox"
      :checked="$store.state.interactiveElementsState[meta.label]"
      @change="change"
    />
    <span>
      {{ text }}
    </span>
  </label>
</template>

<script>
import { labelToText } from "@/helpers";

export default {
  props: ["meta"],
  methods: {
    change(event) {
      this.$store.dispatch("submitAction", {
        label: this.meta.label,
        data: event.target.checked
      });
    }
  },
  computed: {
    text() {
      return labelToText(this.meta.label);
    },
    style() {
      return `button is-${this.meta.type}`;
    }
  }
};
</script>

<style scoped>
input,
span {
  vertical-align: middle;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
</style>
