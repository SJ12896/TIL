<template>
  <div>
    <!-- template태그는 하나의 최상위 태그가 필요하고 그 안에서 작성한다.(보통 div) 안그러면 template안에 같은 태그를 2번 쓸 수 없다. -->
    <h2>New Component</h2>
    {{ myMessage }}
    <input @keyup.enter="childInputChange" v-model="childInputData" type="text">
  </div>
</template>

<script>
export default {
  name: 'NewComponent',
  data: function () { // data는 반드시 함수여야 합니다.
    return {
      childInputData: '',
    }
  },
  props: {
    myMessage: { // 여기서는 kebab-case가 아니라 CamelCase로 작성
      type: String,
      required: true, // props 정의는 가능한 상세하게 정의해야 한다. 디버깅이나 유효성 검증에서 좋다.
    }
  },
  methods: {
    childInputChange: function () {
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>

<style>

</style>