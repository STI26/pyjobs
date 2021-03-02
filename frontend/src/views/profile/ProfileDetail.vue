<template>
  <div class="container">
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <div v-else-if="applicant">
      <ApplicantInfo :user="applicant" :isOwner="true" />
      <!-- resumes -->
      <div class="space-between">
        <p>{{ $t('views.profile.profileDetail.yourResumes') }}:</p>
        <router-link :to="{ name: 'ResumeCreate' }" class="btn-floating">
          <i class="material-icons">add</i>
        </router-link>
      </div>
      <div v-if="applicant.resumes" class="block-resumes">
        <router-link
          v-for="resume of applicant.resumes"
          :key="resume.id"
          :to="{ name: 'ResumeDetail', params: { id: resume.id } }"
          >{{ resume.position }}</router-link
        >
      </div>
      <p v-else>{{ $t('views.profile.profileDetail.noResumes') }}</p>
      <div class="divider"></div>
      <!-- vacancies -->
      <div class="space-between">
        <p>{{ $t('views.profile.profileDetail.yourVacancies') }}:</p>
        <router-link :to="{ name: 'VacancyCreate' }" class="btn-floating">
          <i class="material-icons">add</i>
        </router-link>
      </div>
      <div v-if="applicant.vacancies" class="block-vacancies">
        <router-link
          v-for="vacancy of applicant.vacancies"
          :key="vacancy.id"
          :to="{ name: 'VacancyDetail', params: { id: vacancy.id } }"
          >{{ vacancy.position }}</router-link
        >
      </div>
      <p v-else>{{ $t('views.profile.profileDetail.noVacancies') }}</p>
      <div class="divider mb-2"></div>
      <!-- educations -->
      <EducationInfo
        :educations="additionalUserInfo.educations"
        :isOwner="true"
      />
      <!-- works -->
      <WorkInfo :works="additionalUserInfo.works" :isOwner="true" />
    </div>
    <p v-else>{{ $t('views.profile.profileDetail.noInfo') }}</p>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import ApplicantInfo from '@/components/resume/ApplicantInfo.vue'
import EducationInfo from '@/components/resume/EducationInfo'
import WorkInfo from '@/components/resume/WorkInfo'

export default {
  components: {
    ApplicantInfo,
    EducationInfo,
    WorkInfo
  },
  setup: () => {
    const applicant = ref(null)
    const additionalUserInfo = ref(null)
    const loading = ref(true)
    const store = useStore()
    const router = useRouter()

    const age = d => {
      const d1 = new Date().getTime()
      const d2 = new Date(d).getTime()
      return Math.floor((d1 - d2) / (1000 * 60 * 60 * 24 * 364.25))
    }

    const formatVacancy = companies => {
      const vacancies = []
      companies.forEach(el => {
        const inx = vacancies.findIndex(i => i.id === el.vacancies__id)
        if (el.vacancies__id && inx === -1) {
          vacancies.push({
            id: el.vacancies__id,
            position: el.vacancies__position
          })
        }
      })
      return vacancies
    }

    onMounted(async () => {
      const id = store.getters.userid
      loading.value = true
      store
        .dispatch('getUserInfo', id)
        .then(userInfo => {
          applicant.value = {
            name: `${userInfo.first_name} ${userInfo.last_name}`,
            email: userInfo.email,
            vacancies: formatVacancy(userInfo.company)
          }

          if (userInfo.applicant) {
            return store.dispatch('getAdditionalUserInfo', userInfo.applicant)
          } else {
            router.push('/profile/edit')
            return null
          }
        })
        .then(adUserInfo => {
          additionalUserInfo.value = adUserInfo

          applicant.value.age = age(adUserInfo.date_of_birth)
          applicant.value.bio = adUserInfo.bio
          applicant.value.photo = adUserInfo.photo
          applicant.value.resumes = adUserInfo.resumes

          loading.value = false
        })
        .catch(error => {
          console.warn(error)
        })
    })

    return {
      applicant,
      additionalUserInfo,
      loading
    }
  }
}
</script>

<style lang="scss" scoped>
.block-resumes, .block-vacancies {
  padding: .5rem;

  a {
    margin: 0 .7rem;
  }
}
.mb-2 {
  margin-bottom: 2rem;
}
.space-between {
  display: flex;
  justify-content: space-between;
}
</style>
