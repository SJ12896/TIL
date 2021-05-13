<template>
  <div id="app">
    <h1>This is App</h1>
    <p>AppData: {{ appData }}</p>
    <input type="text" v-model="appData">
    <p>ParentData: {{ parentData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Parent :appData="appData" @parent-input="inputParent"
    @child-input="inputChild"/>
  </div>
</template>

<script>
import Parent from './components/Parent.vue'

export default {
  name: 'App',
  components: {
    Parent,
  },
  data: function () {
      return {
        appData: '',
        parentData: '',
        childData: '',
      }
    },
    methods: {
      inputParent: function (fromParent) {
        this.parentData = fromParent
      },
      inputChild: function (fromChild) {
        this.childData = fromChild
      }
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
