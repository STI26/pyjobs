<template>
  <div>
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <div v-if="data">
      <VacancyListBlock :vacansies="data" />
      <Paginator :paginator="paginator" />
    </div>
    <div class="nothing" v-else>
      <p>{{ $t('views.vacancy.vacancyList.noVacancies') }}</p>
    </div>
    <router-link
      to="/newvacancy"
      class="add-vacancy-btn btn-floating btn-large waves-effect waves-light"
      ><i class="material-icons">add</i></router-link
    >
  </div>
</template>

<script>
import VacancyListBlock from '@/components/vacancy/VacancyListBlock.vue'
import Paginator from '@/components/Paginator.vue'
import { ref, watchEffect } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

export default {
  name: 'Vacancy',
  components: {
    VacancyListBlock,
    Paginator
  },
  setup: () => {
    const data = ref([])
    const paginator = ref({})
    const loading = ref(true)
    const store = useStore()
    const route = useRoute()

    watchEffect(() => {
      loading.value = true
      store.dispatch('getVacancies', route.query).then(res => {
        data.value = res.results
        paginator.value = res.paginator
        loading.value = false
      })
    })

    return {
      data,
      paginator,
      loading
    }
  }
}
</script>

<style lang="scss" scoped>
.add-vacancy-btn {
  position: fixed;
  opacity: 0.5;
  bottom: 2rem;
  right: 2rem;

  &:hover {
    opacity: 1;
  }
}
.nothing {
  padding: 1rem;
}
</style>
