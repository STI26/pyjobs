import { createI18n } from 'vue-i18n'
import en from './languages/english.json'
import ru from './languages/russian.json'

const messages = {
  en,
  ru
}

const browserLang = navigator.language.split('-')[0]

const i18n = createI18n({
  locale: browserLang in messages ? browserLang : 'en',
  fallbackLocale: 'en',
  messages
})

export default i18n
