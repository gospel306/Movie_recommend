import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: false,
    window:{
      width:0,
      height:0
    },
    server: 'http://localhost:8000',
  }
})
