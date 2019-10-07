import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: false,
    leftNavNum:0,
    rightNavNum:0,
    server: 'http://localhost:8000',
  }
})
