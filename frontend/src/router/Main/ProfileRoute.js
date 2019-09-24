import ProfilePage from '@/views/ProfilePage'
import ProfileInfo from '@/components/profile/ProfileInfo'
import ProfileRatingList from '@/components/profile/ProfileRatingList'

export default [
    {
        path: '/profile',
        name: 'profileMain',
        component: ProfilePage
    },
    {
        path: '/profileInfo',
        name: 'profileInformation',
        component: ProfileInfo
    },
    {
        path: '/profileRatingList',
        name: 'profileRatingsList',
        component: ProfileRatingList
    },


    
]
