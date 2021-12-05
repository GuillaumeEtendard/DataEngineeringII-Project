<template>
  <div id='container'>
    <h1>Sentiment analyzer</h1>
    <div id='form'>
      <textarea v-model="message" placeholder="Enter your sentence"></textarea>
      <br/>
      <button v-on:click="test">Submit</button>
    </div>
    <div id="result">
      {{ result }}
    </div>
  </div>
</template>


<script>
import { ref } from "vue";
import axios from 'axios'

export default {
  name: 'Sentiment',
  setup() {
    const result = ref(null)
    const message = ref('')

    return {
      message,
      result
    }
  },
  methods: {
    async test() {
      const response = await axios.get('http://localhost:8000')
      this.result = response.data.message
      return true
    }
  }
}
</script>