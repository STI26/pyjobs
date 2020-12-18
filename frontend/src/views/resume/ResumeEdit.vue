<template>
  <div class="container">
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <div v-else-if="resume" class="forms-wraper">
      <ResumeForm :dataForm="resume" />
    </div>
    <p v-else>Данного резюме нет в базе.</p>
  </div>
</template>

<script>
import ResumeForm from '@/components/resume/ResumeForm'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'

export default {
  components: {
    ResumeForm
  },
  setup: () => {
    const loading = ref(true)
    const resume = ref(null)
    const store = useStore()
    const route = useRoute()

    onMounted(() => {
      const id = route.params.id
      loading.value = true
      store
        .dispatch('getResume', id)
        .then(data => {
          resume.value = data
          loading.value = false
        })
    })

    return {
      loading,
      resume
    }
  }
}
</script>

<style lang="scss" scoped>
.forms-wraper {
  display: flex;
  flex-direction: column;
  padding: 2rem;

  & > form {
    margin-bottom: 3rem;
  }
}
</style>
