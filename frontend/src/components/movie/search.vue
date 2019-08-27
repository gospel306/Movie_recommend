<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <v-container>
          <v-form ref="form">
            <v-layout>
              <v-flex xs3>
                <v-select
                  v-model="T_option"
                  :items="T_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
              <v-flex xs3>
                <v-select
                  v-model="G_option"
                  :items="G_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
              <v-flex xs6>
                <v-text-field v-model="value" />
              </v-flex>
            </v-layout>
            <v-layout justify-center pa-10>
              <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
            </v-layout>
          </v-form>
        </v-container>
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs7>
        <MovieList :MovieItems="movieLists" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import MovieList from "./MovieList";
import axios from "axios";
export default {
  components: {
    MovieList
  },
  data: () => ({
    value: "",
    T_options: [
      { text: "제목", value: "title" },
      { text: "장르", value: "genre" }
    ],
    T_option: "title",
    G_options: [
      { text: "조회수", value: "countrating" },
      { text: "평점", value: "avgrating" }
    ],
    G_option: "countrating",
    movieLists: [],
    params: ""
  }),
  computed: {},
  
  methods: {
    onSubmit() {
      this.params = this.T_option +"="+ this.value + "&order="+ this.G_option;
      axios
        .get(this.$store.state.server + "/api/movies/?" + this.params)
        .then(res => {
          this.movieLists = res.data;
        });
    }
  }
};
</script>
