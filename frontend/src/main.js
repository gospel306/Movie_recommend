import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import VueSession from 'vue-session'

Vue.use(VueSession)
Vue.config.productionTip = false

router.beforeEach(function (to, from, next) {
  if (store.state.login === false && !(to.path == '/index' ||to.path == '/' || to.path == '/search' || to.path == '/login' || to.path == '/signup')) {
    alert("권한이 없습니다");
    next("/");
  } else  {
    next();
  }
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
