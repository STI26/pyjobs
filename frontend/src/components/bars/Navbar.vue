<template>
  <div class="navbar-fixed">
    <ul id="userMenu" class="dropdown-content">
      <template v-if="!auth">
        <li><a class="modal-trigger" href="#modal-login">Вход</a></li>
        <li><a class="modal-trigger" href="#modal-register">Регистрация</a></li>
      </template>
      <template v-else>
        <li><router-link :to="{ name: 'ProfileDetail' }">{{ username }}</router-link></li>
        <li class="divider"></li>
        <li><a @click="logout" href="#!">Выход</a></li>
      </template>
    </ul>
    <nav class="grey lighten-1">
      <div class="nav-wrapper">
        <ul>
          <li v-if="includeSidebarMenu">
            <a
              href="#"
              data-target="slide-out"
              class="sidenav-trigger"
              @click.prevent="$emit('click')"
            >
              <i class="material-icons">menu</i>
            </a>
          </li>
          <router-link to="/" v-slot="{ href, isActive }">
            <li :class="[ isActive && 'active' ]"><a :href="href">PyJobs</a></li>
          </router-link>
          <router-link to="/resume" v-slot="{ href, isActive }">
            <li :class="[ isActive && 'active' ]"><a :href="href">Резюме</a></li>
          </router-link>
          <router-link to="/vacancy" v-slot="{ href, isActive }">
            <li :class="[ isActive && 'active' ]"><a :href="href">Вакансии</a></li>
          </router-link>
          <!-- Dropdown Trigger -->
          <li class="right">
            <a
              class="dropdown-trigger"
              href="#"
              ref="userMenu"
              data-target="userMenu"
              ><i class="material-icons">account_circle</i></a
            >
          </li>
        </ul>
      </div>
    </nav>
    <Login />
    <Register />
  </div>
</template>

<script>
import M from 'materialize-css'
import { ref, onMounted, onUnmounted, computed } from 'vue'
import Login from '@/components/auth/Login.vue'
import Register from '@/components/auth/Register.vue'
import { useStore } from 'vuex'

export default {
  components: { Login, Register },
  props: {
    includeSidebarMenu: Boolean
  },
  setup: () => {
    const userMenu = ref(null)
    let dropdown = null
    const store = useStore()
    const auth = computed(() => store.getters.ifAuthenticated)
    const username = computed(() => store.getters.username)

    const logout = () => {
      store.commit('clearAuth')
    }

    onMounted(() => {
      dropdown = M.Dropdown.init(userMenu.value, {
        constrainWidth: false,
        coverTrigger: false
      })
    })

    onUnmounted(() => {
      if (dropdown && dropdown.destroy) {
        dropdown.destroy()
      }
    })

    return {
      userMenu,
      username,
      auth,
      logout
    }
  }
}
</script>

<style lang="scss" scoped></style>
