import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: []
  },
  mutations: {
    // 존나 중요한 일을 하기 때문에 이름을 대문자로 작성한다. 데이터를 조작하는 함수라고 바로 알 수 있도록
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem);
    },
    DELETE_TODO: function (state, todoItem) {
      const idx = state.todos.indexOf(todoItem)
      return state.todos.splice(idx, 1)
    },
    UPDATE_TODO: function (state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          // spread syntax : 
          return { ...todo, completed: !todo.completed }
        }
        return todo
      })

    }
  },
  actions: {
    // context를 분해? destructuring. 원래 actions의 첫 인자는 context인데 context를 해체해서 그 안의 commit만 사용하도록 했다.
    createTodo: function ({ commit }, todoItem) {
      // context.commit('CREATE_TODO', todoItem)
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function({commit}, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodo: function ({commit}, todoItem) {
      commit('UPDATE_TODO', todoItem)
    }
  },
  // 원래 없었는데 내가 작성
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed !== true
      }).length
    }
  },
  modules: {
  }
})
