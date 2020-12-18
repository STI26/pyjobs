<template>
  <div class="container">
    <AdditionalUserForm v-if="additionalUserInfo" :dataForm="additionalUserInfo" redirectTo="/profile/" />
  </div>
</template>

<script>
import AdditionalUserForm from '@/components/users/AdditionalUserForm.vue'
import { onMounted, ref } from 'vue'
import { useStore } from 'vuex'

export default {
  components: {
    AdditionalUserForm
  },
  setup: () => {
    const store = useStore()
    const additionalUserInfo = ref(null)

    onMounted(() => {
      const id = store.getters.userid
      store
        .dispatch('getUserInfo', id)
        .then(data => {
          if (data.applicant) {
            return store.dispatch('getAdditionalUserInfo', data.applicant)
          } else {
            return { newProfile: true }
          }
        })
        .then(data => {
          additionalUserInfo.value = data
        })
        .catch(error => {
          console.warn(error)
        })
    })

    return {
      additionalUserInfo
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 2rem 1rem;
}
</style>
