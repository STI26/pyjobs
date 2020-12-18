import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import M from 'materialize-css'

const routes = [
  {
    path: '/',
    name: 'Home',
    meta: { layout: 'base-layout' },
    component: () => import('../views/Home.vue')
  },
  {
    path: '/resume',
    name: 'ResumeList',
    meta: { layout: 'advanced-layout' },
    component: () => import('../views/resume/ResumeList.vue')
  },
  {
    path: '/newresume',
    name: 'ResumeCreate',
    meta: { layout: 'base-layout', onlyAuth: true },
    component: () => import('../views/resume/ResumeCreate.vue')
  },
  {
    path: '/resume/:id/',
    name: 'ResumeDetail',
    meta: { layout: 'base-layout' },
    component: () => import('../views/resume/ResumeDetail.vue')
  },
  {
    path: '/resume/:id/edit',
    name: 'ResumeEdit',
    meta: { layout: 'base-layout', onlyAuth: true },
    component: () => import('../views/resume/ResumeEdit.vue')
  },
  {
    path: '/profile/',
    name: 'ProfileDetail',
    meta: { layout: 'base-layout', onlyAuth: true },
    component: () => import('../views/profile/ProfileDetail.vue')
  },
  {
    path: '/profile/edit',
    name: 'ProfileEdit',
    meta: { layout: 'base-layout', onlyAuth: true },
    component: () => import('../views/profile/ProfileEdit.vue')
  },
  {
    path: '/vacancy',
    name: 'VacancyList',
    meta: { layout: 'advanced-layout' },
    component: () => import('../views/vacancy/VacancyList.vue')
  },
  {
    path: '/newvacancy',
    name: 'VacancyCreate',
    meta: { layout: 'base-layout', onlyAuth: true },
    component: () => import('../views/vacancy/VacancyCreate.vue')
  },
  {
    path: '/vacancy/:id/',
    name: 'VacancyDetail',
    meta: { layout: 'base-layout' },
    component: () => import('../views/vacancy/VacancyDetail.vue')
  },
  {
    path: '/vacancy/:id/edit',
    name: 'VacancyEdit',
    meta: { layout: 'base-layout', onlyAuth: true },
    component: () => import('../views/vacancy/VacancyEdit.vue')
  },
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    meta: { layout: 'blank-layout', onlyAuth: false },
    component: () => import('../views/404.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const ifAuthenticated = store.getters.ifAuthenticated
  const onlyAuth = to.matched.some(r => r.meta.onlyAuth)

  if (onlyAuth && !ifAuthenticated) {
    M.toast({ html: 'Эта опция доступна только зарегистрированным пользователям.' })
  } else {
    next()
  }
})

export default router
