<template>
  <div class="container">
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <div v-else-if="resume">
      <ApplicantInfo :user="resume.owner_info" :isOwner="isOwner" />
      <ResumeDetailBlock :resume="resume" :isOwner="isOwner" />
    </div>
    <p v-else>{{ $t('views.resume.resumeDetail.noResume') }}</p>
  </div>
</template>

<script>
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
import ApplicantInfo from '@/components/resume/ApplicantInfo.vue'
import ResumeDetailBlock from '@/components/resume/ResumeDetailBlock.vue'

export default {
  components: {
    ApplicantInfo,
    ResumeDetailBlock
  },
  setup: () => {
    const resume = ref(null)
    const loading = ref(true)
    const store = useStore()
    const route = useRoute()
    const isOwner = computed(() => {
      return (resume.value && (store.getters.userid === resume.value.owner_info.user_id))
    })

    onMounted(async () => {
      const id = route.params.id
      loading.value = true
      resume.value = await store.dispatch('getResume', id)
      loading.value = false
    })

    return {
      resume,
      isOwner,
      loading
    }
  }
}
</script>
