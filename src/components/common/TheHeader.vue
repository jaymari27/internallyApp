<template>
  <section>
    <h1><ion-icon class="logo" name="leaf"></ion-icon>internally</h1>
  </section>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Petit+Formal+Script&display=swap");

section {
  background-color: rgb(141, 212, 132);
  text-align: left;
  box-shadow: 0.5px 1px 3px rgb(158, 158, 158);
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 998;
  overflow: hidden;
}

h1,
.logo {
  cursor: pointer;
}

h1 {
  font-family: "Petit Formal Script", cursive;
  font-size: 1.75rem;
  color: white;
  padding: 1.5rem;
  font-weight: bold;
}

.logo {
  font-size: 2.5rem;
  float: left;
  text-align: center;
  padding: 0 0.5rem;
  transform: scaleX(-1);
}

/* h1,
.logo {
  display: inline;
} */
</style>
