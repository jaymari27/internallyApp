<template>
  <div id="app">
    <the-header />
    <router-view />
  </div>
</template>

<script>
import TheHeader from "./components/TheHeader.vue";

export default {
  components: {
    TheHeader
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=ABeeZee&display=swap");

* {
  margin: 0;
  font-family: "ABeeZee", sans-serif;
}

body {
  font-size: 20px;
  background-color: rgb(236, 236, 236);
}
</style>
