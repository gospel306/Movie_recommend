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
    leftNavNum:17,
    rightNavNum:18,
    leftTemp:[],
    rightTemp:[],
    server: 'http://localhost:8000',
  }
})
