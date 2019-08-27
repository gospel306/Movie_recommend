import MainPage from '../views/MainPage.vue'

import MovieRoute from './Main/MovieRoute.js'
import UserRoute from './Main/UserRoute.js'

export default {
    path: '/',
    name: 'mainpage',
    component: MainPage,
    children: [
        ...MovieRoute,
        ...UserRoute,
    ]
}