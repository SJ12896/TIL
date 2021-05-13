<template>
  <div id="app">

    <h1>YOUTUBE</h1>
    <div class="search">
    <SearchBar @input-search="onInputSearch"/>
    </div>

    <div class="justify">
      <div class="videoScreen">
      <VideoDetail :video="selectedVideo" />
      </div>
      <div class="videoList">
      <VideoList :videos="videos" @select-video="onVideoSelect"/>
      </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'
// key같은 민감한 정보는 코드에 넣지 않고 환경 변수 (따로 파일에 분리) .gitignore에 보면 여기 추가되어있다.
// const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyD-d27hF7XE-Mp0xdsCF3CokzpqE6f1yBg'

export default {
  name: 'App',
  data: function () {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: '',
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    onInputSearch: function (inputText) {
      this.inputValue = inputText
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue
      }
      axios.get(API_URL, {
        params,
      })
      .then((res) => {
        this.videos = res.data.items
        this.selectedVideo = this.videos[0]
      })
      .catch((err) => {
        console.log(err)
      })
    },
    onVideoSelect: function (video) {
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.search {
  margin: 40px;
}
.justify {
  display: flex;
  justify-content: space-between;
}
.videoScreen {
  flex: 2;
}
.videoList {
  flex: 1;
}
</style>
