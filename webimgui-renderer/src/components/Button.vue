<template>
  <button :class="style" @mousedown="down" @mouseup="up">{{ text }}</button>
</template>

<script>
import { labelToText } from "@/helpers";

export default {
  props: ["meta"],
  methods: {
    click() {
      this.$store.dispatch("submitAction", {
        label: this.meta.label,
        data: true
      });
    },
    down() {
      this.$store.dispatch("submitAction", {
        label: this.meta.label,
        data: true
      });
    },
    up() {
      this.$store.dispatch("submitAction", {
        label: this.meta.label,
        data: false
      });
    }
  },
  computed: {
    text() {
      return labelToText(this.meta.label);
    },
    style() {
      return `button is-${this.meta.type}`
    }
  }
};
</script>

<style scoped>
.button {
  margin-bottom: 0.5rem;
}
</style>
