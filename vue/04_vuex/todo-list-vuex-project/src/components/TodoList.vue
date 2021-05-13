<template>
  <div>
    <!-- <TodoListItem v-for="(todo, idx) in $store.state.todos" :key="idx"/> -->
    <TodoListItem v-for="(todo, idx) in todos" :key="idx" :todo="todo"/>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    // todos: function () {
    //   // 여기서는 앞에 this를 붙여줘야 한다.
    //   return this.$store.state.todos
    // }
    ...mapState([ // state를 computed와 mapping? 뭔말인지 / mapgetters, mapactions
      'todos',
    ])
  }
}
</script>

<style>

</style>