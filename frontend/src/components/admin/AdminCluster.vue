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
          <v-radio-group v-model="radio" row>
            <v-radio label="K-Means" value="K-Means"></v-radio>
            <v-radio label="Hierarchical" value="Hierarchical"></v-radio>
            <v-radio label="EM" value="EM"></v-radio>
          </v-radio-group>
          <v-select v-model="option" :items="options" item-text="text" item-value="value" />
        </v-container>
      </v-flex>
    </v-layout>
    <v-layout justify-center wrap>
      <v-flex xs6>
        <v-slider v-model="parameter" label="파라미터" max="100"></v-slider>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      radio: "",
      parameter: 10,
      option: "user",
      options: [
        { text: "유저", value: "user" },
        { text: "영화", value: "movie" }
      ]
    };
  },
  mounted() {},
  methods: {}
};
</script>

<style>
</style>
