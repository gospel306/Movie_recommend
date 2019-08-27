<template>
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
          <v-text-field v-model="T_value" :label="optionLabel" />
        </v-flex>
      </v-layout>
      <v-layout justify-center pa-10>
        <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
      </v-layout>
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    value: "",
    T_options: ["제목", "장르"],
    T_option: "제목",
    G_options: ["조회수순", "평점순"],
    G_option: "조회수순",
    movieList: [],
  }),
  computed: {
    optionLabel() {
      return "영화 " + this.T_option;
    }
  },
  methods: {
    onSubmit() {
      axios
        .get(this.$store.state.server + "/movies", {
          title: this.value
        })
        .then(res => {
          this.movieList = res.data;
        });
    }
  }
};
</script>
