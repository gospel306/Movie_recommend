<template>
  <v-container>
    <v-layout row fill-height >
      <h1>영화관리</h1>
      <v-progress-circular :size="50" color="primary" indeterminate v-if="loading"/>
    </v-layout>
    <v-layout row>
      <v-btn to="/adminuser" color="grey darken-2" class="white--text">유저관리</v-btn>
      <v-btn to="/adminmovie" color="grey darken-2" class="white--text">영화관리</v-btn>
      <v-btn to="/cluster" color="grey darken-2" class="white--text">클러스터</v-btn>
      <v-spacer></v-spacer>
      <v-btn @click="Dialog" color="grey darken-2" class="white--text">수정</v-btn>
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
    <v-dialog v-model="updateDialog">
      <v-card>
        <v-card-title class="headline">영화 정보 수정</v-card-title>
        <v-text-field label="id" v-model="id" readonly="readonly" />
        <v-text-field label="title" v-model="title" />
        <v-text-field label="genres" v-model="genres" />
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-2" class="white--text" @click="update">확인</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      id: "",
      title: "",
      genres: "",
      updateDialog: false,
      selected: [],
      singleSelect: false,
      loading: false,
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
      this.loading = true;
      axios.get(this.$store.state.server + "/api/movies/").then(res => {
        this.desserts = res.data;
        this.loading = false;
      });
    },
    Dialog() {
      if (this.selected.length === 1) {
        this.updateDialog = true;
        this.id = this.selected[0].id;
        this.title = this.selected[0].title;
        this.genres = this.selected[0].genres;
      } else {
        alert("하나만 선택해주세요");
      }
    },
    update() {
      if (this.$session.get("id") == "admin") {
        axios
          .put(
            this.$store.state.server +
              "/api/movies/?id=" +
              this.id +
              "&title=" +
              this.title +
              "&genres=" +
              this.genres
          )
          .then(() => {
            this.updateDialog = false;
            this.getMovieList();
          });
      }
    },
    remove() {
      if (this.$session.get("id") === "admin") {
        for (let i = 0; i < this.selected.length; i++) {
          axios
            .delete(
              this.$store.state.server +
                "/api/movies/?id=" +
                this.selected[i].id
            )
            .then(() => {
              this.getMovieList();
            });
        }
      }
    }
  }
};
</script>

<style>
</style>
