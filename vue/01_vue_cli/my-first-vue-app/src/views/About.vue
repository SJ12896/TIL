<template>
  <div>
    <h1>this is about page</h1>
    <NewComponent my-message="this is prop data" @child-input-change="parentGetChange"/>
  </div>
</template>

<script>
// import NewComponent from '../components/NewComponent.vue'
import NewComponent from '@/components/NewComponent.vue'
// @ === '/src'
// import NewComponent from 'src/components/NewComponent.vue'

export default {
  name: 'About',
  components: {
    NewComponent
  },
  methods: {
    parentGetChange: function (textInput) {
      console.log(`이것은 하위 컴포넌트 NewComponent로 부터 받은 ${textInput}`)
    }
  },
}
</script>

<style scoped>

</style>
