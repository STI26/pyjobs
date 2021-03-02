import { createRouter, createWebHistory } from 'vue-router'
import { nextTick } from 'vue'
import store from '../store'
import M from 'materialize-css'
import i18n from '@/localization/index'

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
    meta: { layout: 'advanced-layout', title: i18n.global.t('router.titles.resumeList') },
    component: () => import('../views/resume/ResumeList.vue')
  },
  {
    path: '/newresume',
    name: 'ResumeCreate',
    meta: { layout: 'base-layout', onlyAuth: true, title: i18n.global.t('router.titles.createResume') },
    component: () => import('../views/resume/ResumeCreate.vue')
  },
  {
    path: '/resume/:id/',
    name: 'ResumeDetail',
    meta: { layout: 'base-layout', title: i18n.global.t('router.titles.resumeDetail') },
    component: () => import('../views/resume/ResumeDetail.vue')
  },
  {
    path: '/resume/:id/edit',
    name: 'ResumeEdit',
    meta: { layout: 'base-layout', onlyAuth: true, title: i18n.global.t('router.titles.resumeEdit') },
    component: () => import('../views/resume/ResumeEdit.vue')
  },
  {
    path: '/profile/',
    name: 'ProfileDetail',
    meta: { layout: 'base-layout', onlyAuth: true, title: i18n.global.t('router.titles.profileDetail') },
    component: () => import('../views/profile/ProfileDetail.vue')
  },
  {
    path: '/profile/edit',
    name: 'ProfileEdit',
    meta: { layout: 'base-layout', onlyAuth: true, title: i18n.global.t('router.titles.profileEdit') },
    component: () => import('../views/profile/ProfileEdit.vue')
  },
  {
    path: '/vacancy',
    name: 'VacancyList',
    meta: { layout: 'advanced-layout', title: i18n.global.t('router.titles.vacancyList') },
    component: () => import('../views/vacancy/VacancyList.vue')
  },
  {
    path: '/newvacancy',
    name: 'VacancyCreate',
    meta: { layout: 'base-layout', onlyAuth: true, title: i18n.global.t('router.titles.vacancyCreate') },
    component: () => import('../views/vacancy/VacancyCreate.vue')
  },
  {
    path: '/vacancy/:id/',
    name: 'VacancyDetail',
    meta: { layout: 'base-layout', title: i18n.global.t('router.titles.vacancyDetail') },
    component: () => import('../views/vacancy/VacancyDetail.vue')
  },
  {
    path: '/vacancy/:id/edit',
    name: 'VacancyEdit',
    meta: { layout: 'base-layout', onlyAuth: true, title: i18n.global.t('router.titles.vacancyEdit') },
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
    M.toast({ html: i18n.global.t('router.accessError') })
  } else {
    next()
  }
})

const DEFAULT_TITLE = 'PyJobs'
router.afterEach((to, from) => {
  nextTick(() => {
    document.title = to.meta.title ? `${DEFAULT_TITLE}: ${to.meta.title}` : DEFAULT_TITLE
  })
})

export default router
