<template>
<!-- 컴포넌트 이름에 the가 붙으면 하위 컴포넌트 없이 단독적일 때 -->
  <div>
    <h2>점심메뉴 추천</h2>
    <button @click="pickOneLunchMenu">메뉴 ㅊㅊ</button>
    <p>오늘 메뉴는 : {{ selectedLunchMenu }}</p>
    <input type="text" v-model="inputNum">
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['간장계란밥', '스팸', '시래기국밥'],
      selectedLunchMenu: '',
      inputNum: 0,
    }
  },
  methods: {
    pickOneLunchMenu: function () {
      this.selectedLunchMenu = _.sample(this.lunch)
      // push : redirect같은거, router-link클릭과 동일한 효과
      this.$router.push({ name: 'TheLotto', params: { lottoNum: this.inputNum }})
    }
  }
}
</script>

<style>

</style>