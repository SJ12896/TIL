<template>
  <div>
    <span @click="updateTodo(todo)" :class="{ completed: todo.completed }">{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    // deleteTodo: function () {
    //   return this.$store.dispatch('deleteTodo', this.todo)
    // },
    // updateTodo: function () {
    //   return this.$store.dispatch('updateTodo', this.todo)
    // }
    ...mapActions([
      'deleteTodo',
      'updateTodo',
    ])
  }
}
</script>

<style scoped>
  .completed {
    text-decoration: line-through;
  }
</style>