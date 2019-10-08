import LoginPage from '@/views/LoginPage'
import SignUpPage from '@/views/SignUpPage'
import IntroPage from '@/views/IntroPage'
export default [
    {
        path: '/login',
        name: 'Login',
        component: LoginPage
    },
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUpPage
    },
    {
        path: '/intro',
        name: 'Intro',
        component: IntroPage
    }
]
