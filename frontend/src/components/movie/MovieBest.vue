<template>
  <v-container align-center text-center class="base">
    <v-layout row wrap fill-height>
      <v-flex sm12>
        <h1>추천 영화</h1>
      </v-flex>
      <v-flex sm12>
        <v-slide-group v-model="model" class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="movie in movies" :key="movie.id" v-slot:default="{ active, toggle }">
            <v-card class="ma-2" height="400" width="250" @click="information(movie.id, movie.average_rating)">
              <v-layout column>
                <v-flex class="top">
                  <v-img 
                  :src="movie.poster" 
                  width="100%"
                  height="100%"
                  ></v-img>
                </v-flex>
                <v-flex class="ca">
                  <h3>{{movie.title}}</h3>
                </v-flex>
              </v-layout>
            </v-card>            
          </v-slide-item>
        </v-slide-group>





      </v-flex>
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
          for(var i = 0; i<this.movies.length;i++){
            if(this.movies[i].title.length > 20)
              this.movies[i].title = this.movies[i].title.substring(0,23)+"..";
          }
        });
    },
  }
};
</script>

<style>
  .base{
    width:95%;
  }
</style>