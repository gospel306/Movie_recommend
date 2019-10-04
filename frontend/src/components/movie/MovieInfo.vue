<template>
  <v-container column justify-content="space-between">
    <v-layout>
      <v-flex xs8>
        <h1>{{this.info.title}}</h1>
        <v-flex>
          <v-layout>
            <h3>평점 -</h3>
            <v-rating
              :value="this.info.average_rating"
              color="black"
              background-color="black"
              half-increments
              dense
              readonly
            />
            <div class="grey--text ml-4">{{ this.info.average_rating.toFixed(1) }}</div>
          </v-layout>
        </v-flex>
        <v-flex>
          <v-layout>
            <h3>장르 -</h3>
            {{this.info.genres}}
          </v-layout>
        </v-flex>
        <v-felx>
            <v-dialog v-model="dialog" persistent max-width="290">
              <template v-slot:activator="{ on }">
                <v-btn color="black white--text" dark v-on="on">평점 작성</v-btn>
              </template>
              <v-card>
                <v-layout justify-center>
                  <v-card-title class="headline">이 영화의 점수는?</v-card-title>
                </v-layout>
                <v-card-text>
                    <v-layout justify-center>별점을 매겨주세요!</v-layout>
                </v-card-text>
                <v-layout justify-center>
                  <v-rating
                    v-model="rating"
                    color="black"
                    dense
                    background-color="black"
                  />
                </v-layout>
                <v-card-actions>
                  <div class="flex-grow-1"></div>
                  <v-btn color="black" text @click="dialog = false; submit()">등록</v-btn>
                  <v-btn color="black" text @click="dialog = false">취소</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
        </v-felx>
      </v-flex>
      <v-flex xs3>
        <v-card
          :color="active ? undefined : 'black'"
          class="ma-4"
          height="400"
          width="300"
        >
          <v-img
            height="100%"
            width="100%"
            v-bind:src="this.info.poster"
          ></v-img>
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout column>
      <h2>줄거리</h2>
      {{movie.plot}}
      <iframe
        v-if="video.length > 0"
        width="100%"
        height="600"
        :src="video"
        frameborder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </v-layout>

    <v-dialog v-model="dialog" dark max-width="60%">
      <v-card>
        <v-card-title>인물 소개</v-card-title>
        <v-card-text>
          <v-layout>
            <v-flex xs3>
              <v-img :src="person.headshot" height="100%" width="100%"></v-img>
            </v-flex>
            <v-flex xs9>
              <v-layout column pl-4>
                <v-flex title>{{person.name}}</v-flex>
                <v-flex>출생 : {{person.birth_date}}</v-flex>
                <v-flex>신장 : {{person.height}}</v-flex>
                <v-flex>
                  - 가족관계 -
                  <v-flex v-for="family in family_member" :key="family">{{family}}</v-flex>
                </v-flex>
                <v-flex>
                  - 이력사항 -
                  <p class="font-weight-thin">{{career}}</p>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      movie: {},
      rating: 0,
      video: "",
      directorlist: [],
      writerlist: [],
      castlist: [],
      main_actor: [],
      more: true,
      dialog: false,
      person: {
        headshot: "",
        name: "",
        birth_date: "",
        height: "",
        spouse: "",
        biography: ""
      },
      family_member: [],
      career: [],
      info:{
        id: 0,
        title: "",
        average_rating: 0,
        genres: "genres",
        contents: "null",
        poster: ""
      },
    };
  },
  mounted() {
    this.MovieInfomation(this.$route.params.id);
    this.rating = this.$route.params.rating;
    axios.get(this.$store.state.server+"/api/movies/?id="+this.$route.params.id).then(res=>{
      console.log(res)
      this.info = res.data[0]
    }).catch(e=>{
      console.log(e)
    })
  },
  methods: {
    MovieInfomation(id) {
      axios
        .get(this.$store.state.server + "/api/moviedetail/?id=" + id)
        .then(res => {
          this.movie = res.data[0];
          if (this.movie.video == "") {
            this.video = "";
          } else {
            this.video = "https://www.youtube.com/embed/" + this.movie.video;
          }
          this.PeopleData();
        });
    },
    PeopleData() {
      for (var i = 0; i < this.movie.directorlist.length; i++) {
        var d = this.movie.directorlist[i].split(":");
        this.directorlist.push({ id: d[0], name: d[1] });
      }
      for (var j = 0; j < this.movie.writerlist.length; j++) {
        var w = this.movie.writerlist[j].split(":");
        this.writerlist.push({ id: w[0], name: w[1] });
      }
      for (var k = 0; k < this.movie.castlist.length; k++) {
        var c = this.movie.castlist[k].split(":");
        this.castlist.push({ id: c[0], name: c[1] });
      }
      for (var k2 = 0; k2 < 5; k2++) {
        var main = this.movie.castlist[k2].split(":");
        this.main_actor.push({ id: main[0], name: main[1] });
      }
    },
    PersonInfo(id) {
      this.dialog = true;
      axios
        .get(this.$store.state.server + "/api/person/?id=" + id)
        .then(res => {
          this.person = res.data[0];
          this.Manufacture(this.person.spouse, this.person.biography);
        });
    },
    Manufacture(family, biography) {
      this.family_member = family.split("|");
      this.career = biography.substring(2, biography.length - 2);
      this.person.birth_date = this.person.birth_date.substring(0, 10);
    },
    CastMore() {
      this.more = false;
    },
    submit(){
      axios.post(this.$store.state.server + "/api/ratings/", {
        userid: this.$session.get('id'),
        movieid: this.info.id,
        rating: this.rating,
        timestamp:"123456789"
      }).catch(e=>{
        console.log(e)
      });
    }
  }
};
</script>

<style>
p {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100%;
}
</style>