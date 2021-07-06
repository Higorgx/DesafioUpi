<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Livros</h1>
        <hr /><br /><br />
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Livro</button>

        <br /><br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Titulo</th>
              <th scope="col">Autor</th>
              <th scope="col">Lido?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">SIM</span>
                <span v-else>NÃO</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                      type="button"
                      class="btn btn-warning btn-sm"
                      v-b-modal.book-update-modal
                      @click="editBook(book)">
                    Atualizar
                  </button>
<<<<<<< Updated upstream
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)">
=======
                 <button
                      type="button"
                      class="btn btn-danger btn-sm"
                      v-b-modal.book-delete-modal
                      @click="onDeleteBook(book)">
>>>>>>> Stashed changes
                    Deletar
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      ref="addBookModal"
      id="book-modal"
      title="Adicionar um novo livro"
      hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="form-title-group"
          label="Titulo:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addBookForm.title"
            required
            placeholder="Titulo"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Autor:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            type="text"
            v-model="addBookForm.author"
            required
            placeholder="Autor"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Lido?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Enviar</b-button>
          <b-button type="reset" variant="danger">Restaurar</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editBookModal"
         id="book-update-modal"
         title="Update"
         hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                label="Titulo:"
                label-for="form-title-edit-input">
                <b-form-input id="form-title-edit-input"
                    type="text"
                    v-model="editForm.title"
                    required
                    placeholder="Entrar titulo">
      </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                  label="Autor:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="text"
                      v-model="editForm.author"
                      required
                      placeholder="Entrar autor">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-read-edit-group">
        <b-form-checkbox-group v-model="editForm.read" id="form-checks">
              <b-form-checkbox value="true">Lido?</b-form-checkbox>
        </b-form-checkbox-group>
    </b-form-group>
    <b-button-group>
      <b-button type="submit" variant="primary">Atualizar</b-button>
      <b-button type="reset" variant="danger">Cancelar</b-button>
    </b-button-group>
  </b-form>
</b-modal>
<<<<<<< Updated upstream
=======
<b-modal ref="DeleteBookModal"
         id="book-delete-modal"
         title="Delete"
         hide-footer>
      <b-form @submit="onDeleteBook"  class="w-100">
      <b-form-group id="form-title-edit-group"
                label="Delete:"
                label-for="form-title-edit-input">
      </b-form-group>
    <b-button-group>
      <b-button type="submit" variant="primary">Atualizar</b-button>
    </b-button-group>
  </b-form>
</b-modal>

>>>>>>> Stashed changes
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      editForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Livro Adicionado!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },

    editBook(book) {
      this.editForm = book;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read,
      };
      this.updateBook(payload, this.editForm.id);
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Livro Atualizado';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      this.initForm();
      this.getBooks(); // why?
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Livro Deletado!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.$refs.DeleteBookModal.hide();
      this.removeBook(book.id);
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
