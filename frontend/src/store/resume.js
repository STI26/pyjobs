import M from 'materialize-css'
import axios from 'axios'
import i18n from '@/localization/index'

const ERROR_MESSAGE = i18n.global.t('store.errorAPI')

export default {
  actions: {
    async getResumes (context, params) {
      try {
        const response = await axios.get('/api/resumes/resume', { params })
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async getResume (context, id) {
      try {
        const response = await axios.get(`/api/resumes/resume/${id}/`)
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async saveResume (context, data) {
      const response = await axios.post('/api/resumes/resume/', data)
      return response
    },
    async updateResume (context, data) {
      const response = await axios.put(`/api/resumes/resume/${data.id}/`, data)
      return response
    },
    async deleteResume (context, id) {
      const response = await axios.delete(`/api/resumes/resume/${id}/`)
      return response
    },
    async getUserInfo (context, id) {
      try {
        const response = await axios.get(`/profile/${id}`)
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async updateUserInfo (context, data) {
      const response = await axios.put(`/profile/${data.id}/`, data)
      return response
    },
    async getAdditionalUserInfo (context, id) {
      try {
        const response = await axios.get(`/api/resumes/applicant/${id}`)
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async saveAdditionalUserInfo (context, data) {
      const response = await axios.post('/api/resumes/applicant/', data, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      return response
    },
    async updateAdditionalUserInfo (context, data) {
      const response = await axios.put(`/api/resumes/applicant/${data.get('id')}/`, data, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      return response
    },
    async getSkills (context) {
      try {
        const response = await axios.get('/api/resumes/skill/')
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async getWork (context, id) {
      try {
        const response = await axios.get(`/api/resumes/work/${id}`)
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async saveWork (context, data) {
      const response = await axios.post('/api/resumes/work/', data)
      return response
    },
    async updateWork (context, data) {
      const response = await axios.put(`/api/resumes/work/${data.id}/`, data)
      return response
    },
    async deleteWork (context, id) {
      const response = await axios.delete(`/api/resumes/work/${id}/`)
      return response
    },
    async getEducation (context, id) {
      try {
        const response = await axios.get(`/api/resumes/education/${id}`)
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async saveEducation (context, data) {
      const response = await axios.post('/api/resumes/education/', data)
      return response
    },
    async updateEducation (context, data) {
      const response = await axios.put(`/api/resumes/education/${data.id}/`, data)
      return response
    },
    async deleteEducation (context, id) {
      const response = await axios.delete(`/api/resumes/education/${id}/`)
      return response
    }
  }
}
