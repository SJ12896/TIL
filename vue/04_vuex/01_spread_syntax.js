const todoItem = {
  todo: '첫 번째 할 일',
  dueDate: '2020-12-25',
  importance: 'high',
  completed: false
}

// completed 값만 변경한다고 가정
//1. 첫 번째 방법
const myUpdateTodo = {
  todo: '첫 번째 할 일',
  dueDate: '2020-12-25',
  importance: 'high',
  completed: true
}

console.log(myUpdateTodo)

//2. 두 번째 방법
const myUpdateTodo2 = {
  ...todoItem,
  // completed가 중간쯤 있으면 어캄? 마지막 꺼를 바꾸는게 아니라 다 불러와놓고 나중에 선언한 값을 덮어씌우는 거
  completed: true
}

console.log(myUpdateTodo2)

const data = { name: 'jin', age: 42, address: 'Seoul' }
const data2 = { name: 'sue', age: 30 }
const data3 = {...data, ...data2}
console.log(data3)