import { createStore } from 'vuex'
import auth from '@/store/auth'
import resume from '@/store/resume'
import vacancy from '@/store/vacancy'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

export default createStore({
  state: {
    token: null,
    userid: null,
    username: null
  },
  getters: {
    username (state) {
      return state.username
    },
    userid (state) {
      return parseInt(state.userid)
    },
    ifAuthenticated (state) {
      return state.token !== null
    }
  },
  mutations: {
    auth (state, userData) {
      state.token = userData.token
      state.userid = userData.user_id
      state.username = userData.username
      // Set localStorege
      localStorage.setItem('token', state.token)
      localStorage.setItem('userid', state.userid)
      localStorage.setItem('username', state.username)
      // Set axios headers
      axios.defaults.headers.common.Authorization = `Token ${state.token}`
    },
    clearAuth (state) {
      state.token = null
      state.userid = null
      state.username = null
      // Clear localStorege
      localStorage.removeItem('token')
      localStorage.removeItem('userid')
      localStorage.removeItem('username')
      // Delete token from axios headers
      delete axios.defaults.headers.common.Authorization
    }
  },
  actions: {},
  modules: {
    auth,
    resume,
    vacancy
  }
})
