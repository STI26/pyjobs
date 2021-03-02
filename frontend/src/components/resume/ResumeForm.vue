<template>
  <!-- Resume form -->
  <form class="col s12" @submit.prevent="saveResume">
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
          {{ $t('components.resume.resumeForm.position') }}
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
          class="validate"
          v-model="form.salary"
        />
        <label for="salary">
          {{ $t('components.resume.resumeForm.salary') }}
        </label>
        <span v-if="errors.salary" class="helper-text red-text">{{
          errors.salary
        }}</span>
      </div>
    </div>
    <div class="row">
      <div ref="chips" class="chips chips-autocomplete col s12">
        <input class="validate" />
      </div>
      <span v-if="errors.nonFieldErrors" class="helper-text red-text">{{
        errors.nonFieldErrors
      }}</span>
    </div>
    <button class="btn waves-effect waves-light" type="submit">
      {{ $t('components.resume.resumeForm.save') }}
      <i class="material-icons right">save</i>
    </button>
  </form>
  <!-- /Resume form -->
</template>

<script>
import M from 'materialize-css'
import { onMounted, onUpdated, reactive, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { setObjFields, setErrorFields, clearObjectFields } from '@/assets/main'
import { useI18n } from 'vue-i18n'

export default {
  props: {
    dataForm: Object
  },
  setup: (props) => {
    const store = useStore()
    const router = useRouter()
    const chips = ref(null)
    let chipsObj = null
    const form = reactive({
      position: '',
      salary: null,
      skills: []
    })
    const errors = reactive({
      position: '',
      salary: null,
      skills: [],
      nonFieldErrors: ''
    })

    const saveResume = () => {
      form.skills = chipsObj.chipsData

      let action
      if (props.dataForm && props.dataForm.id) {
        form.id = props.dataForm.id
        action = 'updateResume'
      } else {
        action = 'saveResume'
      }

      store
        .dispatch(action, form)
        .then(response => {
          clearObjectFields(form)
          clearObjectFields(errors)

          router.push(`/resume/${response.data.id}`)
        })
        .catch(error => {
          setErrorFields(errors, error.response.data)
        })
    }

    const autocompleteSkills = async () => {
      const res = await store.dispatch('getSkills')
      const acc = {}
      res.forEach(el => (acc[el.tag] = null))
      return acc
    }

    onMounted(async () => {
      const { t } = useI18n({ useScope: 'global' })
      // fill form
      props.dataForm && setObjFields(form, props.dataForm)
      // load skills and autocomplete
      chipsObj = M.Chips.init(chips.value, {
        data: form.skills,
        placeholder: t('components.resume.resumeForm.skills'),
        secondaryPlaceholder: '+Tag',
        autocompleteOptions: {
          data: await autocompleteSkills()
        }
      })
    })

    onUpdated(() => {
      M.updateTextFields()
    })

    return {
      form,
      errors,
      chips,
      saveResume
    }
  }
}
</script>
