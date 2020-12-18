<template>
  <div>
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <div v-if="data">
      <ResumeListBlock :resumes="data" />
      <Paginator :paginator="paginator" />
    </div>
    <div class="nothing" v-else>
      <p>Резюме не найдены.</p>
    </div>
    <router-link
        to="/newresume"
        class="add-resume-btn btn-floating btn-large waves-effect waves-light"
      ><i class="material-icons">add</i></router-link
    >
    </div>
</template>

<script>
import ResumeListBlock from '@/components/resume/ResumeListBlock.vue'
import Paginator from '@/components/Paginator.vue'
import { ref, watchEffect } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

export default {
  name: 'Resume',
  components: {
    ResumeListBlock,
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
      store.dispatch('getResumes', route.query)
        .then(res => {
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
.add-resume-btn {
  position: fixed;
  opacity: .5;
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
