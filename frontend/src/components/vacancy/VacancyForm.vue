<template>
  <div>
    <!-- Vacancy form -->
    <form class="col s12" @submit.prevent="saveVacancy">
      <div class="row">
        <div class="input-field col s6">
          <select
            v-model.lazy.number="form.company"
            ref="companyElem"
            class="validate"
            required
          >
            <option value="" disabled selected>
              {{ $t('components.vacancy.vacancyForm.selectCompany') }}</option>
            <option
              v-for="company in companyList.options"
              :key="company.id"
              :value="company.id"
              >{{ company.name }}
            </option>
          </select>
          <label>
            {{ $t('components.vacancy.vacancyForm.company') }}
          </label>
          <span v-if="errors.company" class="helper-text red-text">{{
            errors.company
          }}</span>
        </div>
        <div class="col s6">
          <a class="btn-floating add-company modal-trigger" href="#company-modal">
            <i class="material-icons">add</i>
          </a>
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
          <label for="position">
            {{ $t('components.vacancy.vacancyForm.position') }}
          </label>
          <span v-if="errors.position" class="helper-text red-text">{{
            errors.position
          }}</span>
        </div>
      </div>
      <div class="row">
        <div class="input-field col s4">
          <input
            id="salary"
            type="number"
            min="0"
            class="validate"
            v-model="form.salary"
          />
          <label for="salary">
            {{ $t('components.vacancy.vacancyForm.salary') }}
          </label>
          <span v-if="errors.salary" class="helper-text red-text">{{
            errors.salary
          }}</span>
        </div>
      </div>
      <div class="row">
        <div class="input-field col s12">
          <textarea
            id="description-vacancy"
            class="materialize-textarea validate"
            v-model="form.description"
            required
          ></textarea>
          <label for="description-vacancy">
            {{ $t('components.vacancy.vacancyForm.description') }}
          </label>
        </div>
      </div>
      <button class="btn waves-effect waves-light" type="submit">
        {{ $t('components.vacancy.vacancyForm.save') }}
        <i class="material-icons right">save</i>
      </button>
    </form>
    <!-- /Vacancy form -->
    <!-- Company modal form -->
    <CompanyForm @update-options="updateOptions"  />
  </div>
</template>

<script>
import M from 'materialize-css'
import { onMounted, onUnmounted, onUpdated, reactive, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { setObjFields, setErrorFields, clearObjectFields } from '@/assets/main'
import CompanyForm from '@/components/vacancy/CompanyForm'

export default {
  components: {
    CompanyForm
  },
  props: {
    dataForm: Object
  },
  setup: props => {
    const store = useStore()
    const router = useRouter()
    const companyElem = ref(null)
    const companyList = reactive({ options: [] })
    const form = reactive({
      id: null,
      company: null,
      position: '',
      salary: null,
      description: ''
    })
    const errors = reactive({
      id: null,
      company: null,
      position: '',
      salary: null,
      description: '',
      nonFieldErrors: ''
    })
    let companyObj

    const loadCompanyList = () => {
      const query = {
        owner__id: store.getters.userid
      }
      store
        .dispatch('getCompanies', query)
        .then(response => {
          companyObj.destroy()
          companyList.options.splice(0)
          response.map(i => companyList.options.push(i))
          setTimeout(() => {
            companyObj = M.FormSelect.init(companyElem.value, {})
          }, 0)
        })
        .catch(error => {
          console.warn(error)
        })
    }

    const updateOptions = () => {
      loadCompanyList()
    }

    const saveVacancy = () => {
      const action = form.id ? 'updateVacancy' : 'saveVacancy'

      store
        .dispatch(action, form)
        .then(response => {
          clearObjectFields(form)
          clearObjectFields(errors)

          router.push(`/vacancy/${response.data.id}`)
        })
        .catch(error => {
          setErrorFields(errors, error.response.data)
        })
    }

    onMounted(() => {
      // fill form
      props.dataForm && setObjFields(form, props.dataForm)
      companyObj = M.FormSelect.init(companyElem.value, {})
      loadCompanyList()
    })

    onUpdated(() => {
      M.updateTextFields()
    })

    onUnmounted(() => {
      if (companyObj && companyObj.destroy) {
        companyObj.destroy()
      }
    })

    return {
      form,
      errors,
      companyElem,
      companyList,
      updateOptions,
      saveVacancy
    }
  }
}
</script>

<style lang="scss" scoped>
.add-company {
  margin-top: 1rem;
}
</style>
