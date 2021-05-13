<template>
  <div>
    <ul>
      <VideoListItem v-for="(video, idx) in videos" :key="idx" :video="video" @select-video="onSelectVideo"/>
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  props: {
    videos: Array,
  },
  components: {
    VideoListItem,
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>
h4 {
  margin: 0px;
  text-align: center;
}
</style>