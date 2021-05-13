<template>
  <div>
    <h1>This is Child</h1>
    <p>Child Data: {{ childData }} </p>
    <input type="text" v-model="childData" @input="inputChildData">
    <p>appData: {{ appData }}</p>
    <p>ParentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Parent',
  data: function () {
    return {
      childData: '',
    }
  },
  props: {
    appData: String,
    parentData: String,
  },
  methods: {
    inputChildData: function (){
      this.$emit('child-input', this.childData)
    }
  }
}
</script>

<style>

</style>