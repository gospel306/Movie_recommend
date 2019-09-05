import MoviePage from '@/views/MoviePage'
import MovieSimilar from '@/components/movie/MovieSimilar'
export default [
    {
        path: '/search',
        name: 'moviesearch',
        component: MoviePage
    },
    {
        path: '/similar',
        name: 'moviesimilar',
        component: MovieSimilar,
        props: true
    }
]
