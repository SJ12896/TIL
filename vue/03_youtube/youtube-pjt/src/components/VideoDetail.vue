<template>
<div>
  <div v-if="video" class="iframeDiv">
    <iframe :src="videoURI" frameborder=0 allowfullscreen></iframe>
    </div>
    <h2>{{ video.snippet.title | stringUnescape }}</h2>
    <p>{{ video.snippet.description | stringUnescape }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: [String, Object],
    }
  },
  computed: {
    videoURI: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
    filters: {
    stringUnescape: function (rawText) {
      // 깨지는 문자열 처리 쉽게 lodash사용
      return _.unescape(rawText)
    }
  }
}
</script>

<style>
.iframeDiv {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%
}
iframe {
  /* width: 60vw;
  height: 100vh; */
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
div {
  margin-bottom: 5px;
}
</style>