import axios from 'axios'

export default {
  actions: {
    register ({ commit }, userData) {
      return new Promise((resolve, reject) => {
        const url = '/register/'
        axios
          .post(url, userData)
          .then(res => {
            commit('auth', res.data)
            resolve()
          })
          .catch(res => reject(res))
      })
    },
    login ({ commit }, userData) {
      return new Promise((resolve, reject) => {
        const url = '/login/'
        axios
          .post(url, userData)
          .then(res => {
            commit('auth', res.data)
            resolve()
          })
          .catch(res => reject(res))
      })
    },
    autoLogin ({ commit }) {
      const token = localStorage.getItem('token')
      if (!token) {
        return undefined
      }
      commit('auth', {
        token: localStorage.getItem('token'),
        user_id: localStorage.getItem('userid'),
        username: localStorage.getItem('username')
      })
    }
  }
}
