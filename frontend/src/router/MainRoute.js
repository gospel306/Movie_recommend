import MainPage from '@/views/MainPage.vue'

import MovieRoute from '@/router/Main/MovieRoute.js'
import UserRoute from '@/router/Main/UserRoute.js'
import AdminRoute from '@/router/Main/AdminRoute.js'
import AuthRoute from '@/router/Main/AuthRoute.js'
import ProductRoute from '@/router/Main/ProductRoute.js'

export default {
    path: '/',
    name: 'mainpage',
    component: MainPage,
    children: [
        ...MovieRoute,
        ...UserRoute,
        ...AdminRoute,
        ...AuthRoute,
        ...ProductRoute,
    ]
}
