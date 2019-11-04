<template>
  <div class="select">
    <select :value="$store.state.interactiveElementsState[meta.label]" @change="change">
      <option v-for="choice in meta.choices" :key="choice">{{ choice }}</option>
    </select>
  </div>
</template>

<script>
export default {
  props: ["meta"],
  methods: {
    change(event) {
      this.$store.dispatch("submitAction", {
        label: this.meta.label,
        data: event.target.value
      });
    }
  }
};
</script>

<style scoped>
.select {
  margin-bottom: 0.5rem;
}
</style>
