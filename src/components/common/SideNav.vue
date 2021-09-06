<template>
  <section>
    <div class="nav">
      <div class="user__current">
        <ion-icon class="user__current-icon" name="logo-octocat"></ion-icon>
        <h3 class="user__current-author">
          {{ currentUser.displayname }}
        </h3>
        <h5 class="user__current-slug">@{{ currentUser.username }}</h5>
      </div>
      <div class="btn btn-post" @click="showCompose">
        Create a Thought
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: ["currentUser", "composeIsShown"],
  emit: ["showCompose"],
  methods: {
    showCompose() {
      this.$emit("showCompose", this.composeIsShown);
    }
  }
};
</script>

<style scoped>
div {
  margin: 1rem 0;
}

.nav {
  padding: 0 1rem;
  margin: 0;
  display: flex;
  flex-direction: column;
  position: fixed;
}

.user__current {
  box-shadow: 0.5px 1px 3px rgb(158, 158, 158);
  border-radius: 15px;
  padding: 1.5rem 5rem;
  background-color: white;
  text-align: center;
}

.user__current-slug,
.user__current-author {
  cursor: pointer;
}

.user__current-slug:hover,
.user__current-author:hover {
  color: rgb(141, 212, 132);
}

.user__current-icon {
  font-size: 3rem;
  border-radius: 30px;
  color: white;
  background-color: rgb(140, 119, 196);
}

.user__current-slug {
  color: rgb(153, 153, 153);
}

.btn-post {
  background-color: rgb(141, 212, 132);
  box-shadow: 0.5px 1px 3px rgb(158, 158, 158);
  padding: 0.5rem;
  text-align: center;
  border-radius: 10rem;
  cursor: pointer;
  font-size: 80%;
  font-weight: bold;
  bottom: 0;
}

.btn-post:hover {
  background-color: rgb(124, 206, 113);
}
</style>
