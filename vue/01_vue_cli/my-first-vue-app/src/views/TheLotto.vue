<template>
  <div>
    <h2>lotto 추천</h2>
    <button @click="getLottoNums">ㅂㄴ호 ㅊㅊ</button>
    <!-- <p>{{ $route.params }}</p> -->
    <p>번호는 : {{ selectedLottoNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      sampleNums: [],
      selectedLottoNums: [],
    }
  },
  methods: {
    getLottoNums () {
      const numbers = _.range(1, 46)
      this.sampleNums = _.sampleSize(numbers, this.$route.params.lottoNum)
      this.selectedLottoNums = _.sortBy(this.sampleNums)
      
    }
  }
}
</script>

<style>

</style>