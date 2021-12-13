<template>
  <div id="container" class="container">
    <div class="row mb-3">
      <div class="col-12">
        <h1>Sentiment analyzer</h1>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-12">
        <div id="form">
          <div class="form-floating mb-3">
            <textarea
              class="form-control"
              v-model="message"
              placeholder="Enter your sentence"
              id="floatingTextarea2"
              style="height: 100px"
            ></textarea>
            <label for="floatingTextarea2">Enter your sentence</label>
          </div>
          <button
            v-on:click="submit"
            class="btn btn-primary"
            :disabled="submitting"
          >
            <span
              v-if="submitting"
              class="spinner-border text-light"
              role="status"
            >
              <span class="visually-hidden">Loading...</span>
            </span>
            <span v-else>Predict</span>
          </button>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <div v-if="result" id="result">The text entered is {{ result }}</div>
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from "vue";
import axios from "axios";

export default {
  name: "Sentiment",
  setup() {
    const result = ref(null);
    const message = ref("");
    const submitting = ref(false);

    return {
      message,
      result,
      submitting,
    };
  },
  methods: {
    async submit() {
      this.result = "";
      this.submitting = true;
      const response = await axios.post("http://localhost:8000/get_sentiment", {
        text: this.message,
      });
      this.result = response.data.message;
      this.submitting = false;
    },
  },
};
</script>


<style scoped>
</style>