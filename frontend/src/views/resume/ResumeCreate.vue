<template>
  <div class="container">
    <div v-if="!additionalUserInfo">
      <AdditionalUserForm redirectTo="/newresume" />
    <button>Next</button>
    </div>
    <div v-else>
      <ResumeForm />
    </div>
  </div>
</template>

<script>
import AdditionalUserForm from '@/components/users/AdditionalUserForm.vue'
import ResumeForm from '@/components/resume/ResumeForm'
import { onMounted, ref } from 'vue'
import { useStore } from 'vuex'

export default {
  components: {
    AdditionalUserForm,
    ResumeForm
  },
  setup: () => {
    const store = useStore()
    const additionalUserInfo = ref(null)

    onMounted(async () => {
      const id = store.getters.userid
      const getUserInfo = await store.dispatch('getUserInfo', id)
      additionalUserInfo.value = getUserInfo.applicant
    })

    return {
      additionalUserInfo
    }
  }
}
</script>
