<template>
  <v-container align-center text-center class="base">
    <v-layout row wrap fill-height>
      <v-flex sm12>
        <h1>추천 영화</h1>
      </v-flex>
      <v-flex sm12>
        <v-slide-group v-model="model" class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="movie in movies" :key="movie.id" v-slot:default="{ active, toggle }">
            <v-card
              class="ma-2"
              height="400"
              width="250"
              @click="information(movie.id, movie.average_rating)"
            >
              <v-layout column>
                <v-flex class="top">
                  <v-img :src="movie.poster" width="100%" height="100%"></v-img>
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
      movies: [],
      cluster_movies: [],
      cluster_string: ""
    };
  },
  mounted() {
    this.getMovieList();
  },
  methods: {
    information(id, rating) {
      this.$router.push({
        name: "movieinfo",
        params: { id: id, rating: rating }
      });
    },
    StrEdit(str) {
      this.cluster_string = str;
      this.cluster_string = this.cluster_string.replace("[", "");
      this.cluster_string = this.cluster_string.replace("]", "");
      this.cluster_string = this.cluster_string.replace("(", "");
      this.cluster_string = this.cluster_string.replace(")", "");
      var array = this.cluster_string.split(",");

      for (let index = 1; index < array.length; index += 2) {
        this.cluster_movies.push(array[index]);
      }
    },
    getMovieList() {
      if (this.$session.get("cluster") == "KNN_user") {
        axios
          .get(
            this.$store.state.server +
              "/api/KNN/?user_id=" +
              this.$session.get("id")
          )
          .then(res => {
            this.StrEdit(res.data[0].movie);
            for (let i = 0; i < this.cluster_movies.length; i++) {
              axios
                .get(this.$store.state.server + "/api/movies/?id="+this.cluster_movies[i])
                .then(res => {
                  this.movies.push(res.data[0]);
                  this.titleSkip();
                });
            }
          });
      } else if (this.$session.get("cluster") == "KNN_movie") {
        axios
          .get(
            this.$store.state.server +
              "/api/KNN/?movie_id=" +
              this.$session.get("id")
          )
          .then(res => {
            this.cluster_movies = res.data;
          });
      } else if (this.$session.get("cluster") == "MF") {
        axios
          .get(
            this.$store.state.server +
              "/api/MF/?user_id=" +
              this.$session.get("id")
          )
          .then(res => {
            this.cluster_movies = res.data;
          });
      } else {
        axios.get(this.$store.state.server + "/api/movies/").then(res => {
          this.movies = res.data;
          this.titleSkip();
        });
      }
    },
    titleSkip() {
      for (var i = 0; i < this.movies.length; i++) {
        if (this.movies[i].title.length > 20)
          this.movies[i].title = this.movies[i].title.substring(0, 23) + "..";
      }
    }
  }
};
</script>

<style>
.base {
  width: 95%;
}
</style>