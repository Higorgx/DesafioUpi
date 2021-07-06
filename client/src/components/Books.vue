<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Livros</h1>
        <hr /><br /><br />
          <b-alert
            :show="dismissCountDown"
            dismissible
            @dismissed="dismissCountDown=0"
            @dismiss-count-down="countDownChanged"
            >{{ message }}
          </b-alert>
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
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    v-b-modal.book-delete-modal
                    @click="onShowDelete(book.id)">
                    Deletar
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
         <b-alert variant='danger' v-if="HasBook"
            :show="true"
            >{{HasBook}}
          </b-alert>
          <p  v-show=false v-else>{{HasBook}}</p>
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
            v-model="BookForm.title"
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
            v-model="BookForm.author"
            required
            placeholder="Autor"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="BookForm.read" id="form-checks">
            <b-form-checkbox value="true">Lido?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary" click="ver o que chama isso">Enviar</b-button>
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
                    v-model="BookForm.title"
                    required
                    placeholder="Entrar titulo">
      </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                  label="Autor:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="text"
                      v-model="BookForm.author"
                      required
                      placeholder="Entrar autor">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-read-edit-group">
        <b-form-checkbox-group v-model="BookForm.read" id="form-checks">
              <b-form-checkbox value="true">Lido?</b-form-checkbox>
        </b-form-checkbox-group>
    </b-form-group>
    <b-button-group>
      <b-button type="submit" variant="primary">Atualizar</b-button>
      <b-button type="reset" variant="danger">Cancelar</b-button>
    </b-button-group>
  </b-form>
</b-modal>
<b-modal ref="deleteBookModal"
         id="book-delete-modal"
         title="Deletar"
         hide-footer>
         <b-button-group>
          <b-button
            variant="danger"
            @click="onDeleteBook()">
            Sim
          </b-button>
          <b-button
            variant="primary"
            @click="fecharModal">
            Não
          </b-button>
        </b-button-group>
</b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      HasBook: false,
      bookId: '',
      books: [],
      BookForm: {
        id: 'Null',
        title: '',
        author: '',
        read: 'null',
      },
      message: '',
      dismissCountDown: 0,
    };
  },
  components: {
  },
  methods: {
    hasBooks() {
      if (this.books.length === 0) {
        this.HasBook = 'Não há livros';
      } else {
        this.HasBook = '';
      }
    },
    showAlert(message) {
      this.dismissCountDown = 5;
      this.message = message;
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
          this.hasBooks();
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
          this.showAlert('Livro Adicionado!');
          this.showMessage = true;
          this.hasBooks();
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
      if (this.BookForm.read[0]) read = true;
      const payload = {
        title: this.BookForm.title,
        author: this.BookForm.author,
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
      this.BookForm = book;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      let read = false;
      if (this.BookForm.read[0]) read = true;
      const payload = {
        title: this.BookForm.title,
        author: this.BookForm.author,
        read,
      };
      console.log(this.BookForm.id);
      this.updateBook(payload, this.BookForm.id);
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.showAlert('Livro Atualizado');
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
      this.BookForm.title = '';
      this.BookForm.author = '';
      this.BookForm.read = [];
      this.BookForm.id = '';
      this.BookForm.title = '';
      this.BookForm.author = '';
      this.BookForm.read = 'null';
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.showAlert('Livro Deletado!');
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook() {
      this.removeBook(this.bookId);
      this.$refs.deleteBookModal.hide();
    },
    onShowDelete(bookID) {
      this.bookId = bookID;
      console.log(this.bookId);
    },
    fecharModal() {
      this.$refs.deleteBookModal.hide();
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
