<template>
  <div id="app">
    <the-header> </the-header>
    <!-- hidden modal form -->
    <transition name="fade">
      <modal-form
        v-if="modalIsShown"
        :modalIsShown="modalIsShown"
        @closeModal="closeModal"
        @showModal="showModal"
        :toEdit="toEdit"
        @editThought="editThought"
      ></modal-form>
    </transition>
    <!-- nav area-->
    <div class="layout">
      <!-- side nav -->
      <side-nav
        :composeIsShown="composeIsShown"
        :current-user="currentUser"
        @showCompose="showCompose"
      ></side-nav>

      <!-- main nav (containing all Thoughts/Posts)-->
      <main-nav
        :composeIsShown="composeIsShown"
        :modalIsShown="modalIsShown"
        :current-user="currentUser"
        :thought-list="thoughtList"
        @changeStatus="changeStatus"
        @deleteThought="deleteThought"
        @addNewThought="addNewThought"
        @showModal="showModal"
      ></main-nav>
    </div>

    <div class="overlay" v-if="modalIsShown"></div>
  </div>
</template>

<script>
import TheHeader from "./components/common/TheHeader.vue";

// Navigation
import MainNav from "./components/common/MainNav.vue";
import SideNav from "./components/common/SideNav.vue";

import ModalForm from "./components/common/ModalForm.vue";
// Dummy Data
// import USER_DATA from "./dummy-data";

export default {
  components: {
    TheHeader,
    MainNav,
    SideNav,
    ModalForm
  },
  data() {
    return {
      UID: "marius",
      currentUser: "",
      composeIsShown: false,
      modalIsShown: false,
      toEdit: "",
      userList: [
        {
          id: "marius",
          displayname: "Marius 陆景和",
          username: "MVHKing"
        },
        {
          id: "artem",
          displayname: "Atty. Artem Wing",
          username: "libra"
        },
        {
          id: "vyn",
          displayname: "Dr. Richter",
          username: "the_adjudicator"
        },
        {
          id: "luke",
          displayname: "Luke Pearce",
          username: "lukeoverhere"
        }
      ],
      thoughtList: [
        {
          thought_id: 0,
          author_id: "marius",
          thought_content: "Finish book 1 of the Percy Jackson series",
          isDone: false,
          priority: "low"
        },
        {
          thought_id: 1,
          author_id: "marius",
          thought_content: "MTG with client @ 09/06 10AM, Room401",
          isDone: false,
          priority: "low"
        },
        {
          thought_id: 3,
          author_id: "marius",
          thought_content: "Pick up groceries otw home",
          isDone: false,
          priority: "low"
        },
        {
          thought_id: 4,
          author_id: "marius",
          thought_content:
            "add a ref to the input, Then add a click event to the button,",
          isDone: false,
          priority: "high"
        },
        {
          thought_id: 5,
          author_id: "marius",
          thought_content: "Get started",
          isDone: true,
          priority: "low"
        },
        {
          thought_id: 6,
          author_id: "marius",
          thought_content:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
          // status: "finished",
          isDone: true,
          priority: "low"
        },
        {
          thought_id: 7,
          author_id: "marius",
          thought_content:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu volutpat odio facilisis mauris sit amet massa.",
          // status: "finished",
          isDone: true,
          priority: "low"
        },
        {
          thought_id: 8,
          author_id: "marius",
          thought_content: "sed libero enim sed faucibus",
          isDone: false,
          priority: "low"
        },
        {
          thought_id: 9,
          author_id: "marius",
          thought_content:
            "tempor commodo ullamcorper a lacus vestibulum sed arcu",
          isDone: true,
          priority: "low"
        },
        {
          thought_id: 10,
          author_id: "marius",
          thought_content:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu volutpat odio facilisis mauris sit amet massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu volutpat odio facilisis mauris sit amet massa.",
          isDone: true,
          priority: "low"
        }
      ]
    };
  },
  beforeMount() {
    this.currentUser = this.userList.find(user => user.id === this.UID);
  },
  methods: {
    addNewThought(newThought) {
      this.thoughtList.unshift(newThought); // Add to the beginning of the array
    },
    deleteThought(id) {
      const newThoughtList = this.thoughtList.filter(
        thought => thought.thought_id != id
      );

      this.thoughtList = newThoughtList;
    },
    changeStatus(id) {
      const targetThought = this.thoughtList.find(function(thought) {
        if (thought.thought_id === id) {
          thought.isDone = !thought.isDone;
        }
      });
    },
    showCompose() {
      this.composeIsShown = !this.composeIsShown;
    },
    showModal(data) {
      this.modalIsShown = !data.isShown;

      this.toEdit = this.thoughtList.find(
        thought => thought.thought_id === data.id
      );
    },
    closeModal() {
      this.modalIsShown = !this.modalIsShown;
    },
    editThought(updatedThought) {
      const that = this;
      const targetThought = this.thoughtList.find(function(thought) {
        if (thought.thought_id === that.toEdit.thought_id) {
          thought.thought_content = updatedThought;
          that.modalIsShown = !that.modalIsShown;
        }
      });
    }
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
