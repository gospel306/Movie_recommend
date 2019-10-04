<template>
  <v-container text-center>
    <h1>추천 영화</h1>
    <v-layout row fill-height>
      <v-sheet class="mx-auto" elevation="8" max-width="90%">
        <v-slide-group v-model="model" class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="movie in movies" :key="movie.id" v-slot:default="{ active, toggle }">
            <v-card class="ma-4" height="550" width="300" @click="information(movie.id, movie.average_rating)">
              <v-img :src="movie.poster" height="450"></v-img>
              <h3>{{movie.title}}</h3>
              <h5>{{movie.genres}}</h5>
              <v-rating
                :value="movie.average_rating"
                color="indigo"
                background-color="indigo"
                half-increments
                dense
                readonly
              />
              <v-row class="fill-height" align="center" justify="center">
                <v-scale-transition>
                  <v-icon v-if="active" color="white" size="48" v-text="'mdi-close-circle-outline'"></v-icon>
                </v-scale-transition>
              </v-row>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      model: null,
      movies: []
    };
  },
  mounted() {
    this.getMovieList();
  },
  methods: {
    information(id,rating) {
      this.$router.push({ name: "movieinfo", params: { id: id , rating: rating} });
    },
    getMovieList() {
      axios
        .get(this.$store.state.server + "/api/movies/")
        .then(res => {
          this.movies = res.data;
        });
    },
  }
};
</script>