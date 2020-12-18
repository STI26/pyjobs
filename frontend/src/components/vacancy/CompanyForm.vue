<template>
  <!-- Modal Form -->
  <div class="modal" ref="modalCompany" id="company-modal">
    <form @submit.prevent="onSubmit">
      <div class="modal-content">
        <div class="row">
          <div class="input-field col s12">
            <input
              id="company-name"
              type="text"
              class="validate"
              v-model="form.name"
              required
            />
            <label for="company-name">Название</label>
            <span v-if="errors.name" class="helper-text red-text">{{
              errors.name
            }}</span>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s12">
            <input
              id="email"
              type="email"
              class="validate"
              v-model="form.email"
              required
            />
            <label for="email">Email</label>
            <span v-if="errors.email" class="helper-text red-text">{{
              errors.email
            }}</span>
          </div>
        </div>
        <label v-if="form.photo">
          <input v-model="clearPhoto" type="checkbox" class="filled-in" />
          <span>удалить <a :href="form.photo">ваш логотип</a></span>
        </label>
        <div class="row">
          <div class="file-field input-field col s12">
            <div class="btn">
              <span>Загрузить логотип</span>
              <input type="file" accept="image/png, image/jpeg" @change="onImageChange">
            </div>
            <div class="file-path-wrapper">
              <input class="file-path validate" type="text">
            </div>
          </div>
          <span v-if="errors.photo" class="helper-text red-text">{{
            errors.photo
          }}</span>
        </div>
        <div class="row">
          <div class="input-field col s12">
            <textarea
              id="description"
              class="materialize-textarea validate"
              v-model="form.description"
              required
            ></textarea>
            <label for="description">Описание</label>
            <span v-if="errors.description" class="helper-text red-text">{{
              errors.description
            }}</span>
            <span v-if="errors.nonFieldErrors" class="helper-text red-text">{{
              errors.nonFieldErrors
            }}</span>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <div class="modal-footer__btns">
          <a href="#!" class="btn modal-close waves-effect waves-light red"
            >Отмена</a
          >
          <button
            class="btn waves-effect waves-light"
            type="submit"
            name="action"
          >
            Сохранить
            <i class="material-icons right">send</i>
          </button>
        </div>
      </div>
    </form>
  </div>
  <!-- /Modal Form -->
</template>

<script>
import M from 'materialize-css'
import { onMounted, onUpdated, onUnmounted, ref, reactive } from 'vue'
import { setObjFields, setErrorFields, clearObjectFields } from '@/assets/main'
import { useStore } from 'vuex'

export default {
  props: {
    dataCompany: Object
  },
  setup: (props, { emit }) => {
    const store = useStore()
    const modalCompany = ref(null)
    const clearPhoto = ref(false)
    let photoFile = null
    const form = reactive({
      id: null,
      name: null,
      email: '',
      photo: '',
      description: ''
    })
    const errors = reactive({
      name: null,
      email: '',
      photo: '',
      description: '',
      nonFieldErrors: ''
    })
    let modal

    const onSubmit = () => {
      const action = form.id ? 'updateCompany' : 'saveCompany'

      const formData = new FormData()
      formData.append('name', form.name)
      formData.append('email', form.email)
      formData.append('description', form.description)
      if (clearPhoto.value) {
        formData.append('photo', '')
      } else if (photoFile) {
        formData.append('photo', photoFile)
      }
      if (form.id) {
        formData.append('id', form.id)
      }

      store
        .dispatch(action, formData)
        .then(response => {
          clearObjectFields(form)
          clearObjectFields(errors)
          modal.close()
          emit('update-options')
        })
        .catch(error => {
          if (error.response && error.response.data) {
            setErrorFields(errors, error.response.data)
          }
        })
    }

    const onImageChange = e => {
      const files = e.target.files || e.dataTransfer.files
      if (!files.length) return null
      if (files[0].size > 1048576) {
        M.toast({ html: 'Выберите файл размером до 1 мегабайта.' })
        return null
      }
      photoFile = files[0]
    }

    onMounted(() => {
      if (props.dataCompany && props.dataCompany.id) {
        setObjFields(form, props.dataCompany)
      }
      modal = M.Modal.init(modalCompany.value, {})
    })

    onUpdated(() => {
      M.updateTextFields()
    })

    onUnmounted(() => {
      if (modal && modal.destroy) {
        modal.destroy()
      }
    })

    return {
      modalCompany,
      onSubmit,
      onImageChange,
      clearPhoto,
      form,
      errors
    }
  }
}
</script>
