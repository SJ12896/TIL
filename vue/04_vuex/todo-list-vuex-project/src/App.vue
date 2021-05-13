<template>
  <div id="app">
    <h1>Todo App</h1>
    <h2>completed Todo: {{ completedTodosCount }}</h2>
    <h2>uncompleted Todo: {{ uncompletedTodosCount }}</h2>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed: {
    // completedTodosCount: function () {
    //   return this.$store.getters.completedTodosCount
    // },
    // uncompletedTodosCount: function () {
    //   return this.$store.getters.uncompletedTodosCount
    // }
    ...mapGetters([
      'completedTodosCount',
      'uncompletedTodosCount'
    ])
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
