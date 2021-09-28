<template>
  <div class="thoughts">
    <transition name="fade">
      <div class="thoughts__new-thought" v-if="composeIsShown">
        <form class="new-thought__form" @submit.prevent="addNewThought">
          <textarea
            class="new-thought__compose"
            placeholder="What's on your mind?"
            v-model="newThought"
          />
          <div class="btn-div">
            <button
              class="btn__submit-thought"
              :disabled="!newThought.length > 0"
              @click="addNewThought(-1, newThought)"
            >
              Post
            </button>
          </div>
        </form>
      </div>
    </transition>
    <div v-if="thoughtList.length != 0">
      <transition-group name="fade">
        <div
          class="thoughts__container"
          v-for="(thought, i) in thoughtList.slice().reverse()"
          :key="thought.thought_id"
        >
          <h4 class="thoughts__author">
            Marius 陆景和
          </h4>
          <h5 class="thoughts__author-slug">@MVHKing</h5>
          <p class="thoughts__thought-content">
            {{ thought.thought_content }}
          </p>
          <div class="btn-div">
            <button
              class="btn__edit"
              @click="modalCtrl(thought.thought_id, thought.thought_content)"
              :disabled="thought.is_done"
            >
              Edit
            </button>
            <button
              class="btn__status"
              :class="{ statusOngoing: !thought.is_done }"
              @click="changeStatus(thought.thought_id, thought.is_done)"
            >
              {{ thought.is_done ? "Mark as Not Done" : "Mark as Done" }}
            </button>
            <button
              class="btn__delete"
              @click="deleteThought(thought.thought_id, true)"
            >
              Delete Thought
            </button>
          </div>
        </div>
      </transition-group>
    </div>
    <div class="thoughts__container" v-else>
      No thoughts, head empty.
    </div>
  </div>
</template>

<script>
export default {
  emits: ["modalCtrl"],
  props: ["composeIsShown", "modalIsShown", "updatedThought"],
  data() {
    return {
      newThought: "",
      thoughtList: [],
      path: "http://127.0.0.1:5000/thoughts"
    };
  },
  created() {
    this.getThoughts();
  },
  methods: {
    getThoughts() {
      this.axios
        .get(this.path)
        .then(response => (this.thoughtList = response.data))
        .catch(err => {
          console.error(err);
        });
    },
    editThought(thought_id, thought_content) {
      const data = {
        thought_id: thought_id,
        thought_content: thought_content
      };
      console.log(data);
      this.axios.post(this.path, data).then(() => this.getThoughts());
    },
    changeStatus(thought_id, is_done) {
      const data = {
        thought_id: thought_id,
        is_done: !is_done
      };
      this.axios.post(this.path, data).then(() => this.getThoughts());
    },
    deleteThought(thought_id, to_delete) {
      const data = {
        thought_id: thought_id,
        to_delete: to_delete
      };
      this.axios.post(this.path, data).then(() => this.getThoughts());
    },
    addNewThought(thought_id, thought_content) {
      const data = {
        thought_id: thought_id,
        thought_content: thought_content,
        is_done: false,
        to_delete: false
      };
      this.axios.post(this.path, data).then(() => this.getThoughts());

      this.newThought = ""; // Empty textarea
    },
    modalCtrl(thought_id, thought_content) {
      this.$emit("modalCtrl", {
        isShown: this.modalIsShown,
        thought_id,
        thought_content
      });
      this.editThought(thought_id, this.updatedThought);
    }
  }
};
</script>

<style scoped>
.thoughts {
  padding: 1rem;
  font-size: 85%;
  z-index: 0;
}

.new-thought__compose,
.new-thought__form {
  border-radius: 15px;
}

.new-thought__form {
  background-color: white;
  box-shadow: 0.5px 1px 3px rgb(158, 158, 158);
  margin-bottom: 1rem;
}

.new-thought__compose {
  padding-top: 1.5rem;
  font-size: 100%;
  display: block;
  border: 0;
  width: 95%;
  height: 100%;
  box-sizing: border-box;
  margin: 0 auto 1rem;
  resize: none;
  outline: none;
}

.thoughts__container {
  box-shadow: 0.5px 1px 3px rgb(158, 158, 158);
  border-radius: 15px;
  margin-bottom: 1rem;
  padding: 1rem 2rem;
  background-color: white;
}

.thoughts__author,
.thoughts__author-slug {
  cursor: pointer;
}

.thoughts__author:hover,
.thoughts__author-slug:hover {
  color: rgb(141, 212, 132);
}

.thoughts__thought-content {
  word-break: break-word;
}

.btn__submit-thought {
  background-color: rgb(141, 212, 132);
  border: none;
  width: 10rem;
  box-shadow: 0.5px 1px 3px rgb(158, 158, 158);
  padding: 0.5rem 0;
  margin: 1rem;
  text-align: center;
  border-radius: 10rem;
  cursor: pointer;
  font-size: 90%;
  font-weight: bold;
}

.btn__submit-thought:hover {
  background-color: rgb(124, 206, 113);
}

.btn-div {
  text-align: right;
}

button {
  width: 9rem;
  margin-top: 0.5rem;
  padding: 0.4rem 0;
  text-align: center;
  border-radius: 10rem;
  cursor: pointer;
  font-size: 80%;
  text-transform: capitalize;
}

.btn__status,
.btn__delete {
  background-color: rgb(190, 190, 190);
  border: none;
}

.btn__status:hover {
  background-color: rgb(153, 153, 153);
}

.statusOngoing {
  background-color: rgb(255, 182, 87);
}

.statusOngoing:hover {
  background-color: rgb(255, 164, 45);
}

.btn__delete {
  background-color: rgb(255, 138, 138);
}

.btn__delete:hover {
  background-color: rgb(240, 117, 117);
}

.btn__edit {
  background-color: transparent;
  border: 2px solid rgb(117, 146, 240);
  padding: 0.25rem 0;
}

.btn__edit:hover {
  background-color: rgb(226, 226, 226);
}

h4,
h5 {
  display: inline;
}

h5 {
  color: rgb(153, 153, 153);
}

p {
  padding-top: 1rem;
}

.fade-enter {
  opacity: 0;
}
.fade-enter-active {
  transition: opacity 0.7s;
}
.fade-leave {
}
.fade-leave-active {
  transition: opacity 0.5s;
  opacity: 0;
}
</style>
