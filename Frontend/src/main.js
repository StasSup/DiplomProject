import Vue from 'vue'
import App from './App.vue'
import Element from 'element-ui'
import locale from 'element-ui/lib/locale/lang/ru-RU'
import router from '@/router/router'
import * as VueGoogleMaps from 'vue2-google-maps'
import { settings } from './googleMapApi/settings.js';
import store from './store/store.js';
import './axios.js'

Vue.config.productionTip = false;

Vue.use(VueGoogleMaps, {
  load: settings
})

Vue.use(Element, { locale })

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
