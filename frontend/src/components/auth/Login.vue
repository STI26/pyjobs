<template>
  <!-- Modal Login -->
  <div id="modal-login" class="modal" ref="modalLogin">
    <form @submit.prevent="onSubmit">
      <div class="modal-content">
        <h4>{{ $t("components.auth.login.login") }}</h4>
        <div class="input-field">
          <input
            id="login-username"
            type="text"
            :class="{ invalid: errors.username }"
            class="validate"
            v-model="form.username"
            required
          />
          <label for="login-username">{{ $t("components.auth.login.username") }}</label>
          <span v-if="errors.username" class="helper-text red-text">{{
            errors.username
          }}</span>
        </div>
        <div class="input-field">
          <input
            id="login-password"
            type="password"
            :class="{ invalid: errors.password }"
            class="validate"
            v-model="form.password"
            required
          />
          <label for="login-password">{{ $t("components.auth.login.password") }}</label>
          <span v-if="errors.password" class="helper-text red-text">{{
            errors.password
          }}</span>
          <span
            v-if="errors.nonFieldErrors"
            class="helper-text red-text"
            data-error="wrong"
            >{{ errors.nonFieldErrors }}</span
          >
        </div>
      </div>
      <div class="modal-footer">
        <div class="modal-footer__btns">
          <a href="#!" class="btn modal-close waves-effect waves-light red"
            >{{ $t("components.auth.login.cancel") }}</a
          >
          <button
            class="btn waves-effect waves-light"
            type="submit"
            name="action"
          >
            {{ $t("components.auth.login.enter") }}
            <i class="material-icons right">send</i>
          </button>
        </div>
        <div class="modal-footer__links">
          <a href="#modal-register" class="modal-close modal-trigger"
            >{{ $t("components.auth.login.register") }}</a
          >
        </div>
      </div>
    </form>
  </div>
  <!-- /Modal Login -->
</template>

<script>
import M from 'materialize-css'
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { useStore } from 'vuex'
import { setErrorFields, clearObjectFields } from '@/assets/main'

export default {
  props: {},
  setup: (props) => {
    const modalLogin = ref(null)
    const form = reactive({
      username: '',
      password: ''
    })
    const errors = reactive({
      username: '',
      password: '',
      nonFieldErrors: ''
    })
    let modal = null

    const store = useStore()

    const onSubmit = () => {
      store
        .dispatch('login', form)
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
      modal = M.Modal.init(modalLogin.value, {})
    })

    onUnmounted(() => {
      if (modal && modal.destroy) {
        modal.destroy()
      }
    })

    return {
      modalLogin,
      form,
      errors,
      onSubmit
    }
  }
}
</script>
