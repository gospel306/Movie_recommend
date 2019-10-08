<template>
  <v-container text-center>
    <v-layout row align-center class="sh">
      <v-flex>
        <v-layout justify-center wrap class="under">
          <v-flex xs2> 
            <v-checkbox v-model="selected" label="조회수/평점" value="4" @change="ShowBox"></v-checkbox>
          </v-flex>
          <v-flex xs2> 
            <v-text-field color="black" label="검색어" v-model="value" />
          </v-flex>
          <v-flex xs2> 
            <v-btn large color="red darken-4" class="white--text" @click="onSubmit">Search</v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex class="fir">
        <v-slide-group v-model="model" active-class="success" show-arrows>
          <v-slide-item v-for="movie in movies" :key="movie.id" v-slot:default="{ active, toggle }">
            <v-card class="ma-2" height="400" width="250" @click="showDetail(movie.id)">
              <v-layout column>
                <v-flex class="top">
                  <v-img 
                  :src="movie.poster" 
                  width="100%"
                  height="100%"
                  ></v-img>
                </v-flex>
                <v-flex class="ca">
                  <h3>{{movie.title}}</h3>
                </v-flex>
              </v-layout>
            </v-card>            
          </v-slide-item>
        </v-slide-group>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  components: {
    
  },
  data: () => ({
    model: null,
    movies: [],
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
    showDetail(id){
      this.$router.push({ name: "movieinfo", params:{id: id}
      });
    },
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
          this.movies = res.data;
          for(var i = 0; i<this.movies.length;i++){
            if(this.movies[i].title.length > 20)
              this.movies[i].title = this.movies[i].title.substring(0,23)+"..";
          }
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

<style>
  .under{
    margin-top: 10px;
  }
  .ca{
    margin-top: 10px;
  }
  .sh{

    height : 600px;

  }

  .fir{
    width:100%;
    height:70%;
  }
  .top{
    width:250px;
    height:350px;
  }
</style>
