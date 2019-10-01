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
    leftNum:4,
    rightNum:1,
    leftTemp:[],
    rightTemp:[],
    server: 'http://localhost:8000',
  }
})
