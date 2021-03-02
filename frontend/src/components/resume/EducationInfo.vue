<template>
  <div v-if="educationsData" class="block-educations">
    <div class="block-educations__header">
      <h5>{{ $t('components.resume.educationInfo.education') }}:</h5>
      <a class="btn-floating" @click.prevent="openModal"><i class="material-icons">add</i></a>
    </div>
    <ul class="collection">
      <li
        v-for="education of educationsData"
        :key="education.id"
        class="collection-item"
      >
        <small v-if="isOwner" class="space-between">
          <a href="#" @click.prevent="openModal(education)">
            {{ $t('components.resume.educationInfo.edit') }}
          </a>
          <a href="#" @click.prevent="deleteEducation(education.id)">
            {{ $t('components.resume.educationInfo.delete') }}
          </a>
        </small>
        <p>{{ $t('components.resume.educationInfo.institution') }}: {{ education.institution }}</p>
        <p>{{ $t('components.resume.educationInfo.specialization') }}: {{ education.specialization }}</p>
        <p>{{ $t('components.resume.educationInfo.yearOfEnding') }}: {{ education.year_of_ending }}</p>
      </li>
    </ul>
    <!-- Modal Form -->
    <div class="modal" ref="modalForm">
      <form @submit.prevent="onSubmit">
        <div class="modal-content">
          <h4>{{ $t('components.resume.educationInfo.education') }}</h4>
          <div class="input-field">
            <input
              id="edu-institution"
              type="text"
              :class="{ invalid: errors.institution }"
              class="validate"
              v-model="form.institution"
              required
            />
            <label for="edu-institution">
              {{ $t('components.resume.educationInfo.institution') }}
            </label>
            <span v-if="errors.institution" class="helper-text red-text">{{
              errors.institution
            }}</span>
          </div>
          <div class="input-field">
            <input
              id="edu-specialization"
              type="text"
              :class="{ invalid: errors.specialization }"
              class="validate"
              v-model="form.specialization"
              required
            />
            <label for="edu-specialization">
              {{ $t('components.resume.educationInfo.specialization') }}
            </label>
            <span v-if="errors.specialization" class="helper-text red-text">{{
              errors.specialization
            }}</span>
          </div>
          <div class="input-field">
            <input
              id="edu-year_of_ending"
              type="number"
              :class="{ invalid: errors.year_of_ending }"
              class="validate"
              v-model="form.year_of_ending"
              required
            />
            <label for="edu-year_of_ending">
              {{ $t('components.resume.educationInfo.yearOfEnding') }}
            </label>
            <span v-if="errors.year_of_ending" class="helper-text red-text">{{
              errors.year_of_ending
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
              >{{ $t('components.resume.educationInfo.cancel') }}</a
            >
            <button
              class="btn waves-effect waves-light"
              type="submit"
              name="action"
            >
              {{ $t('components.resume.educationInfo.save') }}
              <i class="material-icons right">send</i>
            </button>
          </div>
        </div>
      </form>
    </div>
    <!-- /Modal Form -->

  </div>
</template>

<script>
import M from 'materialize-css'
import { onMounted, onUnmounted, onUpdated, reactive, ref, toRef } from 'vue'
import { useStore } from 'vuex'
import { setObjFields, setErrorFields, clearObjectFields } from '@/assets/main'

export default {
  props: {
    educations: Array,
    isOwner: Boolean
  },
  setup: props => {
    const store = useStore()
    const modalForm = ref(null)
    const educationsData = toRef(props, 'educations')
    const form = reactive({
      id: null,
      institution: '',
      specialization: '',
      year_of_ending: ''
    })
    const errors = reactive({
      id: null,
      institution: '',
      specialization: '',
      year_of_ending: '',
      nonFieldErrors: ''
    })
    let modal = null

    const updatePage = data => {
      const edu = educationsData.value.filter(e => (e.id === data.id))
      if (edu.length) {
        setObjFields(edu[0], data)
      } else {
        educationsData.value.push(data)
      }
    }

    const onSubmit = () => {
      const action = form.id ? 'updateEducation' : 'saveEducation'

      store
        .dispatch(action, form)
        .then(response => {
          clearObjectFields(form)
          clearObjectFields(errors)
          modal.close()
          updatePage(response.data)
        })
        .catch(error => {
          if (error.response && error.response.data) {
            setErrorFields(errors, error.response.data)
          }
        })
    }

    const deleteEducation = (id) => {
      store
        .dispatch('deleteEducation', id)
        .then(response => {
          educationsData.value.splice(educationsData.value.findIndex(e => e.id === id), 1)
        })
        .catch(error => {
          console.warn(error.response)
        })
    }

    const openModal = (dataForm) => {
      if (dataForm) {
        dataForm && setObjFields(form, dataForm)
      } else {
        clearObjectFields(form)
        clearObjectFields(errors)
      }
      modal.open()
    }

    onMounted(() => {
      modal = M.Modal.init(modalForm.value, {})
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
      educationsData,
      modalForm,
      form,
      errors,
      openModal,
      deleteEducation,
      onSubmit
    }
  }
}
</script>

<style lang="scss" scoped>
.block-educations {
  &__header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }
}
.space-between {
  display: flex;
  justify-content: space-between;
}
</style>
