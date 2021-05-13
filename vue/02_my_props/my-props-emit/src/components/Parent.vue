<template>
  <div>
  <h1>This is Parent</h1>
    <p>Parent Data: {{ parentData }}</p>
    <input type="text" v-model="parentData" @input="parentInput">
    <p>appData: {{ appData }}</p>
    <p>ChildData: {{ childData }} </p>
  <Child :appData="appData" :parentData="parentData"
  @child-input="inputChild"/>
  </div>
</template>

<script>
import Child from  './Child.vue'

export default {
  name: 'Parent',
  props: {
    appData: String,
  },
  components: {
    Child,
  },
  data: function () {
    return {
      parentData:'',
      childData: '',
    }
  },
  methods: {
    inputChild: function(data) {
      this.childData = data
      this.$emit('child-input', this.childData)
    },
    parentInput () {
      this.$emit('parent-input', this.parentData)
    },
  }
}
</script>

<style scoped>

</style>