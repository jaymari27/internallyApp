<template>
  <div id="container">
    <!-- hidden modal form -->
    <transition name="fade">
      <modal-form
        v-if="modalIsShown"
        :modalIsShown="modalIsShown"
        @modalCtrl="modalCtrl"
        :toEdit="toEdit"
        @editThought="editThought"
      ></modal-form>
    </transition>
    <!-- nav area-->
    <div class="layout container-fluid">
      <!-- side nav -->
      <side-nav
        :composeIsShown="composeIsShown"
        @showCompose="showCompose"
      ></side-nav>

      <!-- main nav (containing all Thoughts/Posts)-->
      <main-nav
        :composeIsShown="composeIsShown"
        :modalIsShown="modalIsShown"
        :updatedThought="updatedThought"
        @modalCtrl="modalCtrl"
      ></main-nav>
    </div>

    <div class="overlay" v-if="modalIsShown"></div>
  </div>
</template>

<script>
// Navigation
import MainNav from "./MainNav.vue";
import SideNav from "./SideNav.vue";
import ModalForm from "./ModalForm.vue";

export default {
  components: {
    MainNav,
    SideNav,
    ModalForm
  },
  data() {
    return {
      composeIsShown: false,
      modalIsShown: false,
      toEdit: "",
      updatedThought: ""
    };
  },
  methods: {
    showCompose() {
      this.composeIsShown = !this.composeIsShown;
    },
    modalCtrl(thought_id, thought_content) {
      this.modalIsShown = !this.modalIsShown;
    },
    editThought(updatedThought) {
      this.updatedThought = updatedThought;
    }
  }
};
</script>

<style>
.layout {
  margin-top: 5rem;
  display: grid;
  grid-template-columns: 22rem auto;
  padding: 1rem 25rem;
}

.fade-enter {
  opacity: 0;
}
.fade-enter-active {
  transition: opacity 1s;
}
.fade-leave {
}
.fade-leave-active {
  transition: opacity 1s;
  opacity: 0;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.144);
  box-shadow: 0.5px 1px 3px rgb(41, 41, 41);
  backdrop-filter: blur(1px);
  z-index: 5;
}
</style>
