<template>
  <form @submit.prevent="applyFilter">
    <ul id="slide-out" ref="sidebarEl" class="sidenav sidenav-fixed">
      <a class="sidenav-close right hide-on-large-only" href="#!"><i class="material-icons">close</i></a>
      <li><a class="subheader"><i class="material-icons">filter_list</i>{{ $t("components.bars.sidebar.filter") }}</a></li>
      <li><div class="divider"></div></li>
      <li>
        <div class="row">
          <div class="input-field col s12">
            <input id="filter-position" v-model.lazy.trim="form.search" type="text">
            <label for="filter-position">{{ $t("components.bars.sidebar.position") }}</label>
          </div>
        </div>
      </li>
      <li><div class="divider"></div></li>
      <li><a class="subheader">{{ $t("components.bars.sidebar.salary") }}:</a></li>
      <li class="filter-field">
        <div class="row">
          <div class="input-field col s6">
            <input id="filter-salary-min" v-model.lazy.number="form.min_salary" type="number" min="0">
            <label for="filter-salary-min">{{ $t("components.bars.sidebar.from") }}</label>
          </div>
          <div class="input-field col s6">
            <input id="filter-salary-max" v-model.lazy.number="form.max_salary" type="number" min="0">
            <label for="filter-salary-max">{{ $t("components.bars.sidebar.to") }}</label>
          </div>
        </div>
      </li>
      <li v-if="isResume"><div class="divider"></div></li>
      <li v-if="isResume"><a class="subheader">{{ $t("components.bars.sidebar.age") }}:</a></li>
      <li v-if="isResume" class="filter-field">
        <div class="row">
          <div class="input-field col s6">
            <input id="filter-birth-max" v-model.lazy.number="form.max_birth" type="number" min="0">
            <label for="filter-birth-max">{{ $t("components.bars.sidebar.from") }}</label>
          </div>
          <div class="input-field col s6">
            <input id="filter-birth-min" v-model.lazy.number="form.min_birth" type="number" min="0">
            <label for="filter-birth-min">{{ $t("components.bars.sidebar.to") }}</label>
          </div>
        </div>
      </li>
      <li>
        <button
          class="btn-flat waves-effect blue lighten-3"
          type="submit"
        >
          {{ $t("components.bars.sidebar.apply") }}
        </button>
      </li>
      <li>
        <button
          class="btn-flat waves-effect blue-grey lighten-4"
          type="reset"
          @click="resetForm"
        >
          {{ $t("components.bars.sidebar.reset") }}
        </button>
      </li>
    </ul>
  </form>
</template>

<script>
import M from 'materialize-css'
import { ref, onMounted, onUnmounted, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'

export default {
  setup: () => {
    const router = useRouter()
    const sidebarEl = ref(null)
    const form = reactive({
      search: '',
      min_salary: null,
      max_salary: null,
      min_birth: null,
      max_birth: null
    })
    let sidebar = null

    const isResume = computed(() => router.currentRoute.value.name === 'ResumeList')

    const calcDate = age => {
      const dateOfBirth = new Date()
      dateOfBirth.setFullYear(dateOfBirth.getFullYear() - age)
      return `${dateOfBirth.getFullYear()}-${dateOfBirth.getMonth()}-${dateOfBirth.getDate()}`
    }

    const applyFilter = () => {
      const query = {}
      Object.entries(form).forEach(([k, v]) => {
        if (!(v === null || v === '')) {
          if (k === 'min_birth' || k === 'max_birth') {
            query[k] = calcDate(v)
          } else {
            query[k] = v
          }
        }
      })

      router.replace({
        name: router.currentRoute.value.name,
        query
      })
    }

    const resetForm = () => {
      form.search = ''
      form.min_salary = null
      form.max_salary = null
      form.min_birth = null
      form.max_birth = null
    }

    onMounted(() => {
      sidebar = M.Sidenav.init(sidebarEl.value, {})
    })

    onUnmounted(() => {
      if (sidebar && sidebar.destroy) {
        sidebar.destroy()
      }
    })

    return {
      sidebarEl,
      sidebar,
      applyFilter,
      resetForm,
      isResume,
      form
    }
  }
}
</script>

<style lang="scss" scoped>
  .sidenav {
    margin-top: 64px;
    z-index: 800;

    li:first-of-type {
      margin-top: 0;
    }
    &-close {
      padding: 1rem;
    }

    .filter-field {
      margin-top: -30px;
    }

    button {
      width: 100%;
      height: 100%;
    }
  }
  @media only screen and (max-width : 992px) {
    .sidenav {
      margin-top: 0;

      li:first-of-type {
        margin-top: 2rem;
      }
    }
  }
</style>
