<template>
<div id='container'>
    <h1>Sentiment analyzer</h1>
<div id='form'>
    <textarea v-model="message" placeholder="Enter your sentence"></textarea>
    <br/>
</div>
</div>
</template>

<script>
export default {
  name: 'Sentiment'
}
</script>