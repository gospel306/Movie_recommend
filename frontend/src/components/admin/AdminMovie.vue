<template>
  <v-container>
    <h1>영화관리</h1>
    <v-layout row>
      <v-btn to="/adminuser" color="grey darken-2" class="white--text">유저관리</v-btn>
      <v-btn to="/adminmovie" color="grey darken-2" class="white--text">영화관리</v-btn>
      <v-spacer></v-spacer>
      <v-btn @click="add" color="grey darken-2" class="white--text">추가</v-btn>
      <v-btn @click="remove" color="grey darken-2" class="white--text">삭제</v-btn>
    </v-layout>
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="desserts"
      :single-select="singleSelect"
      item-key="id"
      show-select
      class="elevation-1"
    >
      <template v-slot:top>
        <v-switch v-model="singleSelect" label="Single select" class="pa-3"></v-switch>
      </template>
    </v-data-table>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      selected: [],
      singleSelect: false,
      headers: [
        {
          align: "left",
          text: "넘버",
          value: "id"
        },
        { text: "제목", value: "title" },
        { text: "조회수", value: "view_cnt" },
        { text: "평점", value: "average_rating" },
        { text: "장르", value: "genres" }
      ],
      desserts: []
    };
  },
  mounted() {
    this.getMovieList();
  },
  methods: {
    getMovieList() {
      axios.get(this.$store.state.server + "/api/movies/").then(res => {
        this.desserts = res.data;
      });
    },
    add() {
      if (this.$session.get("id") === "admin") {
        axios.put((this.$store.state.server + "/api/movies/",{
              username: this.profile.username,
              password: this.profile.password,
              age : this.profile.age,
              occupation : this.profile.occupation,
              gender : this.profile.gender
            }).then(function(){
              alert("성공");
            }).catch(function(){
              alert("실패");
            })
        );
      }
    },
    remove() {
      if (this.$session.get("id") === "admin") {
        // axios.delete(this.$store.state.server + "/api/movies/").then(res => {
        //   this.desserts = res.data;
        // });
      }
    }
  }
};
</script>

<style>
</style>
