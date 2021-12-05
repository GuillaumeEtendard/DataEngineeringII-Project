<template>
  <h1>Data Engineering Project</h1>
  <p>developed by Guillaume Etendard, Camille Omnes and Tom Tea</p>
  <Sentiment />
</template>

<script>
import Sentiment from './components/Sentiment.vue'

export default {
  name: 'App',
  components: {
    Sentiment
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
</style>
