import ProfilePage from '@/views/ProfilePage'
import ProfileInfo from '@/components/profile/ProfileInfo'
import NewRating from '@/components/profile/NewRating'
import MyRatingList from '@/components/profile/MyRatingList'

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
        path: '/newRating',
        name: 'newRating',
        component: NewRating
    },
    {
        path: '/myRatingList',
        name: 'myRatingList',
        component: MyRatingList
    },


    
]
