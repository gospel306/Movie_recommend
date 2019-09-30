<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <v-flex xs4>
        <h2>영화 검색</h2>
      </v-flex>
    </v-layout>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <v-container>
          <v-form ref="form">
            <v-layout justify-center wrap>
              <v-flex xs3>
                <v-select
                  v-model="T_option"
                  :items="T_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
              <v-flex xs4>
                <v-text-field label="검색어" v-model="value" />
              </v-flex>
              <v-flex xs2>
                <v-btn large color="indigo white--text" @click="search">Search</v-btn>
              </v-flex>
            </v-layout>
          </v-form>
        </v-container>
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs7>
        <v-progress-circular :size="200" color="primary" indeterminate v-if="loading"/>
        <MovieList :MovieItems="movieLists" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import MovieList from "@/components/profile/ProfileMovieList";
import axios from "axios";
export default {
  components: {
    MovieList
  },
  data: () => ({
    T_options: [
      { text: "제목", value: "title" },
      { text: "장르", value: "genre" }
    ],
    T_option: "title",
    movieLists: [],
  }),
  computed: {},

  methods: {
    search() {
      this.loading = true;
      if (this.T_option == "title") {
        this.params = {
          age: this.A_option,
          occupation: this.O_option,
          gender: this.G_option,
          order: this.V_option,
          title: this.value
        };
      } else {
        this.params = {
          age: this.A_option,
          occupation: this.O_option,
          gender: this.G_option,
          order: this.V_option,
          genre: this.value
        };
      }
      var params = this.params
      axios
        .get(this.$store.state.server + "/api/movies/", {
            params
        })
        .then(res => {
          this.movieLists = res.data;
          this.loading = false;
        });
    },
  }
};
</script>
