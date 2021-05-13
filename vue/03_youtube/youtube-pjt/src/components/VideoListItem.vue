<template>
  <div class="listItem">
    <div @click="selectVideo">
      <img :src="youtubeImageSrc" alt="youtube_thumbnail">
      </div>
      <div class="titleText">
      {{ video.snippet.title | stringUnescape }}
      </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      // 깨지는 문자열 처리 쉽게 lodash사용
      return _.unescape(rawText)
    }
  }
  ,
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  }
}
</script>
<style>
.listItem {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.titleText {
  padding-left: 2px;
}
</style>