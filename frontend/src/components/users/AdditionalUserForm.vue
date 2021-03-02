<template>
  <div class="container">
    <div class="row">
      <form class="col s12" @submit.prevent="saveInfo">
        <div class="row">
          <div class="input-field col s12">
            <textarea
              id="bio"
              class="materialize-textarea validate"
              v-model="form.bio"
              required
            ></textarea>
            <label for="bio">
              {{ $t('components.users.additionalUserForm.about') }}
            </label>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s4">
            <input
              id="year-of-birth"
              type="text"
              class="validate datepicker"
              v-model.lazy="form.date_of_birth"
              ref="dateOfBirthElem"
              required
            />
            <label for="year-of-birth">
              {{ $t('components.users.additionalUserForm.yearOfBirth') }}
            </label>
          </div>
        </div>
        <label v-if="form.photo">
          <input v-model="clearPhoto" type="checkbox" class="filled-in" />
          <span>
            {{ $t('components.users.additionalUserForm.delete') }}
            <a :href="form.photo">{{ $t('components.users.additionalUserForm.photo') }}</a>
          </span>
        </label>
        <div class="row">
          <div class="file-field input-field  col s12">
            <div class="btn">
              <span>{{ $t('components.users.additionalUserForm.loadPhoto') }}</span>
              <input type="file" accept="image/png, image/jpeg" @change="onImageChange">
            </div>
            <div class="file-path-wrapper">
              <input class="file-path validate" type="text">
            </div>
          </div>
        </div>
        <button class="btn waves-effect waves-light" type="submit">
          {{ $t('components.users.additionalUserForm.save') }}
          <i class="material-icons right">send</i>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import M from 'materialize-css'
import { onMounted, onUnmounted, onUpdated, reactive, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { setObjFields, setErrorFields, clearObjectFields } from '@/assets/main'

export default {
  props: {
    dataForm: Object,
    redirectTo: String
  },
  setup: props => {
    const store = useStore()
    const router = useRouter()
    const dateOfBirthElem = ref(null)
    const clearPhoto = ref(false)
    let dateOfBirthObj = null
    let photoFile = null
    const form = reactive({
      id: null,
      bio: '',
      date_of_birth: null,
      photo: null
    })
    const errors = reactive({
      bio: '',
      date_of_birth: '',
      photo: '',
      nonFieldErrors: ''
    })

    const saveInfo = () => {
      const action = form.id ? 'updateAdditionalUserInfo' : 'saveAdditionalUserInfo'

      const formData = new FormData()
      formData.append('bio', form.bio)
      formData.append('date_of_birth', form.date_of_birth)
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
        .then(data => {
          clearObjectFields(form)
          clearObjectFields(errors)

          if (props.redirectTo) {
            router.push(props.redirectTo)
          } else {
            router.push('/profile/')
          }
        })
        .catch(error => {
          setErrorFields(errors, error.response.data)
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
      // fill form
      if (props.dataForm && props.dataForm.id) {
        setObjFields(form, props.dataForm)
      }
      const options = {
        format: 'yyyy-mm-dd',
        defaultDate: new Date()
      }
      dateOfBirthObj = M.Datepicker.init(dateOfBirthElem.value, options)
    })

    onUpdated(() => {
      M.updateTextFields()
    })

    onUnmounted(() => {
      dateOfBirthObj && dateOfBirthObj.destroy()
    })

    return {
      form,
      errors,
      saveInfo,
      onImageChange,
      clearPhoto,
      dateOfBirthElem
    }
  }
}
</script>
