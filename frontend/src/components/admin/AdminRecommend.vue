<template>
  <v-container>
    <v-layout row fill-height>
      <h1>클러스터</h1>
      <v-progress-circular :size="50" color="primary" indeterminate v-if="loading" />
    </v-layout>
    <v-layout row>
      <v-btn to="/adminuser" color="grey darken-2" class="white--text">유저관리</v-btn>
      <v-btn to="/adminmovie" color="grey darken-2" class="white--text">영화관리</v-btn>
      <v-btn to="/cluster" color="grey darken-2" class="white--text">클러스터</v-btn>
      <v-btn to="/recommend" color="grey darken-2" class="white--text">DB관리</v-btn>
      <v-container fluid row>
        <v-radio-group v-model="selected" row>
          <v-radio label="KNN" value="KNN"></v-radio>
          <v-radio label="MF" value="MF"></v-radio>
        </v-radio-group>
       </v-container>
        <v-btn color="grey darken-2" class="white--text" @click="apply">DB업데이트</v-btn>
    </v-layout>
    <v-layout justify-center wrap>
      <v-flex xs6>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      selected: "KNN",
      loading: false
    };
  },
  methods: {
    apply() {
      this.loading = true;
      axios
        .get(
          this.$store.state.server +
            "/api/" +
            this.selected +
            "/?exe=1"
        )
        .then(res => {
          if (res.data) {
            alert("적용되었습니다");
          }
        })
        .catch(error => {
          alert(error);
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>

<style>
</style>
