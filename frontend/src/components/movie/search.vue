<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <v-flex xs4>
        <v-container fluid row>
          <v-checkbox v-model="selected" label="연령대" value="1" @change="ShowBox"></v-checkbox>
          <v-checkbox v-model="selected" label="직업군" value="2" @change="ShowBox"></v-checkbox>
          <v-checkbox v-model="selected" label="성별" value="3" @change="ShowBox"></v-checkbox>
          <v-checkbox v-model="selected" label="조회수/평점" value="4" @change="ShowBox"></v-checkbox>
        </v-container>
      </v-flex>
    </v-layout>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <v-container>
          <v-form ref="form">
            <v-layout>
              <v-flex xs12 v-if="option_1">
                <v-select
                  v-model="A_option"
                  :items="A_options"
                  item-text="text"
                  item-value="value"
                  label="연령대"
                />
              </v-flex>
              <v-flex xs12 v-if="option_2">
                <v-select
                  v-model="O_option"
                  :items="O_options"
                  item-text="text"
                  item-value="value"
                  label="직업군"
                />
              </v-flex>
              <v-flex xs12 v-if="option_3">
                <v-select
                  v-model="G_option"
                  :items="G_options"
                  item-text="text"
                  item-value="value"
                  label="성별"
                />
              </v-flex>

              <v-flex xs12 v-if="option_4">
                <v-select
                  v-model="V_option"
                  :items="V_options"
                  item-text="text"
                  item-value="value"
                  label="조회수/평점순"
                />
              </v-flex>
            </v-layout>
            <v-layout justify-center wrap>
              <v-flex xs3>
                <v-select
                  v-model="T_option"
                  :items="T_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
              <v-flex xs9>
                <v-text-field label="검색어" v-model="value" />
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
        <v-progress-circular :size="200" color="primary" indeterminate v-if="loading"/>
        <MovieList :MovieItems="movieLists" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import MovieList from "@/components/movie/MovieList";
import axios from "axios";
export default {
  components: {
    MovieList
  },
  data: () => ({
    value: "",
    loading: false,
    A_options: [
      { text: "10대", value: "10" },
      { text: "20대", value: "20" },
      { text: "30대", value: "30" },
      { text: "40대", value: "40" },
      { text: "50대", value: "50" }
    ],
    A_option: "",
    O_options: [
      { text: "고등학생", value: "K-12 student" },
      { text: "자영업", value: "self-employed" },
      { text: "과학자", value: "scientist" },
      { text: "경영진", value: "executive/managerial" },
      { text: "작가", value: "writer" },
      { text: "주부", value: "homemaker" },
      { text: "교육자", value: "academic/educator" },
      { text: "프로그래머", value: "programmer" },
      { text: "엔지니어", value: "technician/engineer" },
      { text: "목사", value: "clerical/admin" },
      { text: "영업사원", value: "sales/marketing" },
      { text: "대학생", value: "college/grad student" },
      { text: "변호사", value: "lawyer" },
      { text: "농부", value: "farmer" },
      { text: "예술가", value: "artist" },
      { text: "공예가", value: "tradesman/craftsman" },
      { text: "서비스직", value: "customer service" },
      { text: "은퇴", value: "retired" },
      { text: "의사", value: "doctor/health care" },
      { text: "무직", value: "unemployed" },
      { text: "기타", value: "other" }
    ],
    O_option: "",
    G_options: [{ text: "남자", value: "M" }, { text: "여자", value: "F" }],
    G_option: "",
    V_options: [
      { text: "조회수", value: "countrating" },
      { text: "평점", value: "avgrating" }
    ],
    V_option: "",
    T_options: [
      { text: "제목", value: "title" },
      { text: "장르", value: "genre" }
    ],
    T_option: "title",
    movieLists: [],
    params: {},
    selected: [],
    option_0: false,
    option_1: false,
    option_2: false,
    option_3: false,
    option_4: false
  }),
  computed: {},

  methods: {
    onSubmit() {
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
    ShowBox() {
      if (this.selected.length != 0) {
        this.option_0 = true;
      } else {
        this.option_0 = false;
      }
      if (this.selected.indexOf("1") > -1) {
        this.option_1 = true;
      } else {
        this.option_1 = false;
        this.A_option = "";
      }
      if (this.selected.indexOf("2") > -1) {
        this.option_2 = true;
      } else {
        this.option_2 = false;
        this.O_option = "";
      }
      if (this.selected.indexOf("3") > -1) {
        this.option_3 = true;
      } else {
        this.option_3 = false;
        this.G_option = "";
      }
      if (this.selected.indexOf("4") > -1) {
        this.option_4 = true;
      } else {
        this.option_4 = false;
        this.V_option = "";
      }
    }
  }
};
</script>
