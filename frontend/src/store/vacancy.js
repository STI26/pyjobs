import M from 'materialize-css'
import axios from 'axios'
import i18n from '@/localization/index'

const ERROR_MESSAGE = i18n.global.t('store.errorAPI')

export default {
  actions: {
    async getVacancies (context, params) {
      try {
        const response = await axios.get('/api/vacancies/vacancy', { params })
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async getVacancy (context, id) {
      try {
        const response = await axios.get(`/api/vacancies/vacancy/${id}/`)
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async saveVacancy (context, data) {
      const response = await axios.post('/api/vacancies/vacancy/', data)
      return response
    },
    async updateVacancy (context, data) {
      const response = await axios.put(`/api/vacancies/vacancy/${data.id}/`, data)
      return response
    },
    async deleteVacancy (context, id) {
      const response = await axios.delete(`/api/vacancies/vacancy/${id}/`)
      return response
    },
    async getCompanies (context, params) {
      try {
        const response = await axios.get('/api/vacancies/company', { params })
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async getCompany (context, id) {
      try {
        const response = await axios.get(`/api/vacancies/company/${id}/`)
        return response.data
      } catch (err) {
        M.toast({ html: ERROR_MESSAGE })
      }
    },
    async saveCompany (context, data) {
      const response = await axios.post('/api/vacancies/company/', data, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      return response
    },
    async updateCompany (context, data) {
      const response = await axios.put(`/api/vacancies/company/${data.get('id')}/`, data, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      return response
    },
    async deleteCompany (context, id) {
      const response = await axios.delete(`/api/vacancies/company/${id}/`)
      return response
    }
  }
}
