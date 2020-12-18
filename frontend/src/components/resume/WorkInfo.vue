<template>
  <div v-if="works" class="block__works">
    <div class="block-works__header">
      <h5>Опыт работы:</h5>
      <a class="btn-floating" @click.prevent="openModal"><i class="material-icons">add</i></a>
    </div>
    <ul class="collection">
      <li v-for="work of works" :key="work.id" class="collection-item">
        <small v-if="isOwner" class="space-between">
          <a href="#" @click.prevent="openModal(work)">Редактировать</a>
          <a href="#" @click.prevent="deleteWork(work.id)">Удалить</a>
        </small>
        <p>Организация: {{ work.organization }}</p>
        <p>Позиция: {{ work.position }}</p>
        <p>
          <span>{{ work.join_date }}</span>
          -
          <span v-if="work.termination_date">{{ work.termination_date }}</span>
          <span v-else>по настоящее время</span>
        </p>
      </li>
    </ul>
    <!-- Modal Form -->
    <div class="modal" ref="modalWork">
      <form @submit.prevent="onSubmit">
        <div class="modal-content">
          <h4>Образование</h4>
          <div class="row">
            <div class="input-field col s12">
              <input
                id="organization"
                type="text"
                class="validate"
                v-model="form.organization"
                required
              />
              <label for="organization">Организация</label>
              <span v-if="errors.organization" class="helper-text red-text">{{
                errors.organization
              }}</span>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s12">
              <input
                id="position"
                type="text"
                class="validate"
                v-model="form.position"
                required
              />
              <label for="position">Позиция</label>
              <span v-if="errors.position" class="helper-text red-text">{{
                errors.position
              }}</span>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s6">
              <input
                id="join_date"
                type="text"
                class="datepicker"
                v-model.lazy="form.join_date"
                ref="joinDateElem"
              />
              <label for="join_date">Дата начала работы</label>
              <span v-if="errors.join_date" class="helper-text red-text">{{
                errors.join_date
              }}</span>
            </div>
            <div class="input-field col s6">
              <input
                id="termination_date"
                type="text"
                class="datepicker"
                v-model.lazy="form.termination_date"
                ref="terminationDateElem"
              />
              <label for="termination_date">Дата окончания работы</label>
              <span v-if="errors.termination_date" class="helper-text red-text">{{
                errors.termination_date
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

  </div>
</template>

<script>
import M from 'materialize-css'
import { onMounted, onUnmounted, onUpdated, reactive, ref, toRef } from 'vue'
import { useStore } from 'vuex'
import { setObjFields, setErrorFields, clearObjectFields } from '@/assets/main'

export default {
  props: {
    works: Array,
    isOwner: Boolean
  },
  setup: props => {
    const store = useStore()
    const modalWork = ref(null)
    const worksData = toRef(props, 'works')
    const joinDateElem = ref(null)
    const terminationDateElem = ref(null)
    let joinDateObj = null
    let terminationDateObj = null
    const form = reactive({
      id: null,
      organization: '',
      position: '',
      join_date: '',
      termination_date: ''
    })
    const errors = reactive({
      id: null,
      organization: '',
      position: '',
      join_date: '',
      termination_date: '',
      nonFieldErrors: ''
    })
    let modal = null

    const updatePage = data => {
      const works = worksData.value.filter(e => (e.id === data.id))
      if (works.length) {
        setObjFields(works[0], data)
      } else {
        worksData.value.push(data)
      }
    }

    const onSubmit = () => {
      const action = form.id ? 'updateWork' : 'saveWork'

      if (!form.termination_date.trim()) {
        delete form.termination_date
      }

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

    const deleteWork = (id) => {
      store
        .dispatch('deleteWork', id)
        .then(response => {
          worksData.value.splice(worksData.value.findIndex(e => e.id === id), 1)
        })
        .catch(error => {
          console.warn(error.response)
        })
    }

    const openModal = (dataForm) => {
      if (dataForm) {
        setObjFields(form, dataForm)
      } else {
        clearObjectFields(form)
        clearObjectFields(errors)
      }
      modal.open()
    }

    onMounted(() => {
      modal = M.Modal.init(modalWork.value, {})
      // set dates
      const options = {
        format: 'yyyy-mm-dd',
        defaultDate: new Date()
      }
      joinDateObj = M.Datepicker.init(joinDateElem.value, options)
      terminationDateObj = M.Datepicker.init(terminationDateElem.value, options)
    })

    onUpdated(() => {
      M.updateTextFields()
    })

    onUnmounted(() => {
      if (modal && modal.destroy) {
        modal.destroy()
      }
      joinDateObj && joinDateObj.destroy()
      terminationDateObj && terminationDateObj.destroy()
    })

    return {
      worksData,
      modalWork,
      form,
      errors,
      openModal,
      deleteWork,
      onSubmit,
      joinDateElem,
      terminationDateElem
    }
  }
}
</script>

<style lang="scss" scoped>
.block-works {
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
