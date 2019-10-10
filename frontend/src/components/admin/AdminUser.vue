<template>
  <v-container>
    <v-layout row fill-height>
      <h1>유저관리</h1>
      <v-progress-circular :size="50" color="primary" indeterminate v-if="loading" />
    </v-layout>
    <v-layout row>
      <v-btn to="/adminuser" color="grey darken-2" class="white--text">유저관리</v-btn>
      <v-btn to="/adminmovie" color="grey darken-2" class="white--text">영화관리</v-btn>
      <v-btn to="/cluster" color="grey darken-2" class="white--text">클러스터</v-btn>
      <v-btn to="/recommend" color="grey darken-2" class="white--text">DB관리</v-btn>
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
        <v-card-title class="headline">유저 정보 수정</v-card-title>
        <v-text-field label="id" v-model="id" readonly="readonly" />
        <v-text-field label="age" v-model="age" />
        <v-text-field label="occupation" v-model="occupation" />
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
      age: "",
      occupation: "",
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
        { text: "닉네임", value: "username" },
        { text: "성별", value: "gender" },
        { text: "나이", value: "age" },
        { text: "직업", value: "occupation" },
        { text: "구독정보", value: "cluster"}
      ],
      desserts: []
    };
  },
  mounted() {
    this.getUserList();
  },
  methods: {
    getUserList() {
      this.loading = true;
      axios
        .get(this.$store.state.server + "/api/auth/signup-many/")
        .then(res => {
          this.desserts = res.data;
          this.loading = false;
        });
    },
    Dialog() {
      if (this.selected.length === 1) {
        this.updateDialog = true;
        this.id = this.selected[0].id;
        this.age = this.selected[0].age;
        this.occupation = this.selected[0].occupation;
      } else {
        alert("하나만 선택해주세요");
      }
    },
    update() {
      if (this.$session.get("id") == "admin") {
         axios
           .put(
             this.$store.state.server + "/api/users/?id=" + this.id
             +"&age="+this.age
             +"&occupation="+this.occupation
           )
           .then(() => {
             this.updateDialog = false;
             this.getUserList();
           });
      }
    }
  }
};
</script>

<style>
</style>
