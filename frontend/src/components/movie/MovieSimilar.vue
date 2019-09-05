<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <v-flex xs7>
        <MovieList :MovieItems="movieLists" :check="check"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import MovieList from "@/components/movie/MovieList";
import axios from "axios";
export default {
  components: {
    MovieList
  },
  data: () => ({
    movieLists: [],
    check: false,
  }),
  computed: {},
  mounted() {
    this.getMovieList();
  },
  methods: {
    getMovieList() {
      axios
        .get(
          this.$store.state.server +
            "/api/similar/?movieid=" +
            this.$route.params.id
        )
        .then(res => {
          this.movieLists = res.data;
        });
    }
  }
};
</script>
