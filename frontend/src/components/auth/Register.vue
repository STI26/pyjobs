<template>
  <!-- Modal Login -->
  <div id="modal-register" class="modal" ref="modalRegister">
    <form @submit.prevent="onSubmit">
      <div class="modal-content">
        <h4>Регистрация</h4>
        <div class="row">
          <div class="input-field col s6">
            <input
              id="reg_username"
              type="text"
              :class="{ invalid: errors.username }"
              class="validate"
              v-model="form.username"
              required
            />
            <label for="reg_username">Ник</label>
            <span v-if="errors.username" class="helper-text red-text">{{
              errors.username
            }}</span>
          </div>
          <div class="input-field col s6">
            <input
              id="reg_email"
              type="email"
              :class="{ invalid: errors.email }"
              class="validate"
              v-model="form.email"
            />
            <label for="reg_email">Email</label>
            <span v-if="errors.email" class="helper-text red-text">{{
              errors.email
            }}</span>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s6">
            <input
              id="first_name"
              type="text"
              :class="{ invalid: errors.first_name }"
              class="validate"
              v-model="form.first_name"
            />
            <label for="first_name">Имя</label>
          </div>
          <div class="input-field col s6">
            <input
              id="last_name"
              type="text"
              :class="{ invalid: errors.last_name }"
              class="validate"
              v-model="form.last_name"
            />
            <label for="last_name">Фамилия</label>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s6">
            <input
              id="reg_password"
              type="password"
              :class="{ invalid: errors.password }"
              class="validate"
              v-model="form.password"
              required
            />
            <label for="reg_password">Пароль</label>
            <span v-if="errors.password" class="helper-text red-text">{{
              errors.password
            }}</span>
            <span v-if="errors.nonFieldErrors" class="helper-text red-text">{{
              errors.nonFieldErrors
            }}</span>
          </div>
          <div class="input-field col s6">
            <input
              id="reg_confirm"
              type="password"
              :class="{ invalid: errors.confirm }"
              class="validate"
              v-model="form.confirm"
              required
            />
            <label for="reg_confirm">Пароль ещё раз</label>
            <span v-if="errors.confirm" class="helper-text red-text">{{
              errors.confirm
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
            Зарегистрироватся
            <i class="material-icons right">send</i>
          </button>
        </div>
        <div class="modal-footer__links">
          <a href="#modal-login" class="modal-close modal-trigger">Войти</a>
        </div>
      </div>
    </form>
  </div>
  <!-- /Modal Login -->
</template>

<script>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import M from 'materialize-css'
import { useStore } from 'vuex'
import { setErrorFields, clearObjectFields } from '@/assets/main'

export default {
  props: {},
  setup: () => {
    const modalRegister = ref(null)
    const form = reactive({
      username: '',
      password: '',
      confirm: '',
      first_name: '',
      last_name: '',
      email: ''
    })
    const errors = reactive({
      username: '',
      password: '',
      confirm: '',
      first_name: '',
      last_name: '',
      email: '',
      nonFieldErrors: ''
    })
    let modal = null

    const store = useStore()

    const onSubmit = () => {
      if (form.password !== form.confirm) {
        errors.confirm = 'Пароли должны совпадать.'
        return null
      }
      store
        .dispatch('register', form)
        .then(data => {
          modal.close()
          clearObjectFields(form)
          clearObjectFields(errors)
        })
        .catch(error => {
          setErrorFields(errors, error.response.data)
        })
    }

    onMounted(() => {
      modal = M.Modal.init(modalRegister.value, {})
    })

    onUnmounted(() => {
      if (modal && modal.destroy) {
        modal.destroy()
      }
    })

    return {
      modalRegister,
      form,
      errors,
      onSubmit
    }
  }
}
</script>
