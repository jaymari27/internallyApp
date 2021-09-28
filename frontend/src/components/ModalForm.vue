<template>
  <div class="modal-form">
    <div class="modal-wrapper">
      <div class="modal-compose">
        <form class="modal-compose__form" @submit.prevent="editThought">
          <textarea
            class="modal-compose__text"
            placeholder="What's on your mind?"
            v-model="current_content"
          />
          <button
            class="btn__submit-thought"
            @disabled="current_content.length > 0"
            @click="editThought"
          >
            Save Changes
          </button>
          <button class="btn__cancel" @click="modalCtrl">Cancel</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["toEdit"],
  emits: ["modalCtrl", "editThoughts"],
  data() {
    return {
      current_content: "",
      thought_id: ""
    };
  },
  methods: {
    editThought() {
      this.$emit("editThought", this.current_content);
      this.modalCtrl();
    },
    modalCtrl() {
      this.$emit("modalCtrl", this.modalIsShown);
    }
  },
  beforeMount() {
    this.thought_id = this.toEdit.thought_id;
    this.current_content = this.toEdit.thought_content;
  }
};
</script>

<style scoped>
.modal-form {
  position: fixed;
  z-index: 999;
  transition: opacity 0.3s ease;
  vertical-align: middle;
  box-shadow: 0.5px 1px 3px rgb(158, 158, 158);
  border-radius: 15px;
  background-color: white;
  margin: 3rem 52rem;
  text-align: center;
  width: 30%;
  box-shadow: 0.5px 1px 10px rgb(158, 158, 158);
}

.modal-compose__text {
  background-color: rgb(245, 245, 245);
  margin: 1rem auto;
  padding: 1.5rem 1rem;
  font-size: 90%;
  display: block;
  border: 0;
  width: 90%;
  min-height: 20vh;
  max-height: 43vh;
  box-sizing: border-box;
  resize: none;
  border-radius: 15px;
  outline: none;
}

.btn__submit-thought {
  background-color: rgb(141, 212, 132);
  border: none;
  width: 10rem;
  padding: 0.5rem 0;
  margin: 1rem 0;
  border-radius: 10rem;
  cursor: pointer;
  font-size: 90%;
  font-weight: bold;
}

.btn__submit-thought:hover {
  background-color: rgb(124, 206, 113);
}

.btn__cancel {
  background-color: white;
  border: 2px solid rgb(180, 180, 180);
  width: 10rem;
  padding: 0.4rem 0;
  margin: 1rem 0;
  border-radius: 10rem;
  cursor: pointer;
  font-size: 90%;
  font-weight: bold;
}

.btn__cancel:hover {
  background-color: rgb(230, 230, 230);
}
</style>
