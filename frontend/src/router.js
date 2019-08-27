import Vue from 'vue';
import Router from 'vue-router'
import MainRoute from './router/MainRoute.js'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        MainRoute,
    ],
  })