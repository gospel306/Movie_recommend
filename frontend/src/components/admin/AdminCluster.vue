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
    </v-layout>
    <v-layout justify-center wrap>
      <v-flex xs6>
        <v-container fluid row>
          <v-radio-group v-model="selected" row>
            <v-radio label="K-Means" value="K-Means"></v-radio>
            <v-radio label="Hierarchical" value="Hierarchical"></v-radio>
            <v-radio label="EM" value="EM"></v-radio>
          </v-radio-group>
          <v-select v-model="option" :items="options" item-text="text" item-value="value" />
        </v-container>
      </v-flex>
    </v-layout>
    <v-layout justify-center wrap>
      <v-flex xs6 row>
        <v-slider v-model="parameter" label="파라미터" max="20"></v-slider>
        <v-btn color="grey darken-2" class="white--text" @click="apply">적용</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      selected: "K-Means",
      loading: false,
      parameter: 10,
      option: "movie",
      options: [
        { text: "영화", value: "movie" },
        { text: "유저", value: "user" }
      ]
    };
  },
  mounted() {},
  methods: {
    apply() {
      this.loading = true;
      axios
        .get(
          this.$store.state.server +
            "/api/cluster/?type=" +
            this.selected +
            "&data=" +
            this.option +
            "&clusteringnum=" +
            this.parameter
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
