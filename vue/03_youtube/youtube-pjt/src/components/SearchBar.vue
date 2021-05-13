<template>
  <div>
    <input @keypress.enter="onInputKeyword" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputKeyword: function (event) {
      this.$emit('input-search', event.target.value)
    }
  }
}
</script>

<style>

</style>