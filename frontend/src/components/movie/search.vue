<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <v-container>
          <v-form ref="form">
            <v-layout>
              <v-flex xs3>
                <v-select v-model="T_option" :items="T_options" />
              </v-flex>
              <v-flex xs3>
                <v-select v-model="G_option" :items="G_options" />
              </v-flex>
              <v-flex xs6>
                <v-text-field v-model="value" :label="optionLabel" />
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
    T_options: ["제목", "장르"],
    T_option: "제목",
    G_options: ["조회수", "평점"],
    G_option: "조회수",
    movieLists: [],
    params : ""
  }),
  computed: {
    optionLabel() {
      return "영화 " + this.T_option;
    }
  },
  methods: {
    onSubmit() {
      if(this.T_option == "제목" ){
        if(this.G_option == "조회수"){
          this.params = "title="+ this.value +"&order=countrating";
        }
        else{
          this.params = "title="+ this.value +"&order=avgrating";
        }
      }
      else{
        if(this.G_option == "조회수"){
          this.params = "genre="+ this.value +"&order=countrating";
        }
        else{
          this.params = "genre="+ this.value +"&order=avgrating";
        }
      }
      axios
        .get(this.$store.state.server + "/api/movies/?" + this.params)
        .then(res => {
          this.movieLists = res.data;
        });
    }
  }
};
</script>
