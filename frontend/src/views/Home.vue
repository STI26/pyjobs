<template>
  <div class="container">
    <div class="row">
      <div class="col s12">
        <ul ref="targetSearch" class="tabs">
          <li class="tab">
            <a data-value="ResumeList" href="#resume">
              {{ $t('views.home.resumes') }}
            </a>
          </li>
          <li class="tab">
            <a data-value="VacancyList" href="#vacancy">
              {{ $t('views.home.vacancies') }}
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="row">
      <div class="col s12">
        <div class="nav-wrapper">
          <form @submit.prevent="search" ref="searchFormElem" class="search-field">
            <div class="input-field">
              <input v-model="query" id="search" type="search" required>
              <label class="label-icon" for="search"><i class="material-icons">search</i></label>
              <i class="material-icons" @click="searchFormElem.reset">close</i>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import M from 'materialize-css'
import { onMounted, onUnmounted, ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
  setup: () => {
    const targetSearch = ref(null)
    const searchFormElem = ref(null)
    const query = ref(null)
    const router = useRouter()
    let tabs = null

    const search = () => {
      if (!query.value.trim()) {
        return null
      }
      const target = tabs.$activeTabLink[0].dataset.value
      router.push({
        name: target,
        query: {
          search: query.value
        }
      })
    }

    onMounted(() => {
      tabs = M.Tabs.init(targetSearch.value, {})
      tabs.select('resume')
    })

    onUnmounted(() => {
      if (tabs) {
        tabs.destroy()
      }
    })

    return {
      targetSearch,
      searchFormElem,
      query,
      search
    }
  }
}
</script>

<style lang="scss" scoped>
$tabs-color: #2196f3;

.container {
  padding-top: 3rem;
  width: 100%;
  height: 80vh;
}
.search-field {
  border: 1px solid #2196f3;
  border-radius: 2rem;

  .input-field {
    margin: 1rem .3rem !important;
    input {
      border-radius: 2rem;
    }
  }
}
.tabs {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: center;

  .tab {
    a {
      color: $tabs-color;
      &.active {
        color: $tabs-color;
      }
      &:hover {
        color: $tabs-color;
      }
      &:focus {
        background-color: rgba($tabs-color, 0.1);
        &.active {
          background-color: rgba($tabs-color, 0.1);
        }
      }
    }
  }
  ::v-deep(.indicator) {
    background-color: $tabs-color!important;
  }
}
</style>
