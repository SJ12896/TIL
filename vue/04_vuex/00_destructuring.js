const context = {
  commit: function () {
    console.log('안녕하세요 commit!')
  },
  state: {
    todo: '할 일 1',
  },
  getters: {},
  mutations: {},
}

//1. 하나 하나 할당
// const commit = context.commit
// const state = context.state

// console.log(commit())
// console.log(state)

//2. 이름으로 가져온다.
// const { commit, state } = context
// console.log(commit())
// console.log(state)

// const { commit } = context
// console.log(commit())

// ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

let a = 1;
let b = 2;
[b, a] = [a, b]
console.log(a, b)

// var c = 3
// var d = 4
// [c, d] = [d, c]
// console.log(c, d)

// const info = { test: 'abc', run: 'def' }
// let { test: new_test, run: new_run } = info
// console.log(new_test, new_run)