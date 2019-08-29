<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <v-flex xs5>
        <v-container fluid row>
          <v-checkbox v-model="selected" label="연령대" value="1" @change="ShowBox"></v-checkbox>
          <v-checkbox v-model="selected" label="직업군" value="2" @change="ShowBox"></v-checkbox>
          <v-checkbox v-model="selected" label="성별" value="3" @change="ShowBox"></v-checkbox>
          <v-checkbox v-model="selected" label="제목/장르" value="4" @change="ShowBox"></v-checkbox>
          <v-checkbox v-model="selected" label="조회수/평점" value="5" @change="ShowBox"></v-checkbox>
        </v-container>
      </v-flex>
    </v-layout>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <v-container>
          <v-form ref="form">
            <v-layout>
              <v-flex xs12 v-if="_1">
                <v-select
                  v-model="A_option"
                  :items="A_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
              <v-flex xs12 v-if="_2">
                <v-select
                  v-model="O_option"
                  :items="O_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
              <v-flex xs12 v-if="_3">
                <v-select
                  v-model="G_option"
                  :items="G_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
              <v-flex xs12 v-if="_4">
                <v-select
                  v-model="T_option"
                  :items="T_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
              <v-flex xs12 v-if="_5">
                <v-select
                  v-model="V_option"
                  :items="V_options"
                  item-text="text"
                  item-value="value"
                />
              </v-flex>
            </v-layout>
            <v-layout justify-center wrap>
              <v-flex xs12 v-if="_0">
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
    A_options: [
      { text: "10대", value: "10" },
      { text: "20대", value: "20" },
      { text: "30대", value: "30" },
      { text: "40대", value: "40" },
      { text: "50대", value: "50" }
    ],
    A_option: "10",
    O_options: [
      { text: "고등학생 이하", value: "K-12 student" },
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
    O_option: "K-12 student",
    G_options: [{ text: "남자", value: "남" }, { text: "여자", value: "여" }],
    G_option: "남",
    T_options: [
      { text: "제목", value: "title" },
      { text: "장르", value: "genre" }
    ],
    T_option: "title",
    V_options: [
      { text: "조회수", value: "countrating" },
      { text: "평점", value: "avgrating" }
    ],
    V_option: "countrating",
    movieLists: [],
    params: "",
    selected: [],
    _0: false,
    _1: false,
    _2: false,
    _3: false,
    _4: false,
    _5: false
  }),
  computed: {},

  methods: {
    onSubmit() {
      this.params =
        this.T_option + "=" + this.value + "&order=" + this.V_option;
      axios
        .get(this.$store.state.server + "/api/movies/?" + this.params)
        .then(res => {
          this.movieLists = res.data;
        });
    },
    ShowBox() {
      if (this.selected.length != 0) {
        this._0 = true;
      } else {
        this._0 = false;
      }
      if (this.selected.indexOf("1") > -1) {
        this._1 = true;
      } else {
        this._1 = false;
      }
      if (this.selected.indexOf("2") > -1) {
        this._2 = true;
      } else {
        this._2 = false;
      }
      if (this.selected.indexOf("3") > -1) {
        this._3 = true;
      } else {
        this._3 = false;
      }
      if (this.selected.indexOf("4") > -1) {
        this._4 = true;
      } else {
        this._4 = false;
      }
      if (this.selected.indexOf("5") > -1) {
        this._5 = true;
      } else {
        this._5 = false;
      }
    }
  }
};
</script>
