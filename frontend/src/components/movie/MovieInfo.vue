<template>
  <v-container fluid class="base" grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs9>
        <v-layout row>
          <v-flex xs11>
            <v-layout row wrap>
              <v-flex xs12>
                <h1>{{this.info.title}}</h1>
              </v-flex>
              <v-flex xs5>
                <h3>{{this.info.genres}}</h3>
              </v-flex>
              <v-flex xs7>
                <v-layout row>
                  <v-flex xs3>
                    <v-rating
                      :value="this.info.average_rating"
                      color="black"
                      background-color="black"
                      half-increments
                      dense
                      readonly
                    />
                  </v-flex>
                  <v-flex x4 class="pa-0">
                    <v-tooltip right>
                      <template v-slot:activator="{ on }">
                        <v-btn text color="white" @click="dialog=true" dark v-on="on">
                          <v-icon large color="red darken-2" v-on="on">mdi-plus</v-icon>
                        </v-btn>
                      </template>
                      <span>평점등록하기</span>
                    </v-tooltip>
                    <v-dialog v-model="dialog" persistent max-width="290">
                      <v-card>
                        <v-layout justify-center>
                          <v-card-title class="headline">이 영화의 점수는?</v-card-title>
                        </v-layout>
                        <v-card-text>
                          <v-layout justify-center>별점을 매겨주세요!</v-layout>
                        </v-card-text>
                        <v-layout justify-center>
                          <v-rating v-model="rating" color="red darken-2" dense background-color="#bdbdbd" />
                        </v-layout>
                        <v-card-actions>
                          <div class="flex-grow-1"></div>
                          <v-btn color="black" text @click="dialog = false; submit()">등록</v-btn>
                          <v-btn color="black" text @click="dialog = false">취소</v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                  </v-flex>
                </v-layout>
              </v-flex>
              <v-flex xs12>
                <v-flex xs6>
                  감독 :<a class="black--text" @click="PersonInfo(directorlist[0].id)">{{directorlist[0].name}}</a>
                </v-flex>
                <v-flex xs12>
                  출연진:
                  <template v-for="i in 3">
                    <a class="black--text" @click="PersonInfo(castlist[i].id)" :key="i">{{castlist[i].name}}, </a>
                  </template>
                </v-flex>
              </v-flex>
              <v-flex xs12 v-if="movie.plot.length==0">
                죄송합니다. 줄거리가 아직 등록되지 않았습니다.
              </v-flex>
              <v-flex xs12 v-if="!this.state && this.movie.plot.length > 300">
                {{movie.plot.substring(1,300)}}
              </v-flex>
              <v-flex xs12 v-if="this.state">
                {{movie.plot.substring(1,2000)}}
              </v-flex>
              <v-btn
                text
                color="black"
                v-if="!this.state && this.movie.plot.length > 300"
                @click="turnState()"
              >..확장
              </v-btn>
              <v-btn text color="black" v-if="this.state" @click="turnState()">..축소</v-btn>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex xs3>
        <v-layout align-center>
          <v-flex>
            <v-img
              class="vi"
              float:right
              height="100%"
              width="100%"
              v-bind:src="this.info.poster"
              @click="Viewtrailer"
            ></v-img>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>

    <v-dialog v-model="trailerDialog" dark max-width="80%">
      <iframe
        v-if="video.length > 0"
        width="100%"
        height="600"
        :src="video"
        frameborder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </v-dialog>

    <v-dialog v-model="personDialog"  max-width="60%" >
      <v-card >
        <v-card-title class="justify-center"><h3>인물소개</h3></v-card-title>
        <v-card-text>
          <v-layout>
            <v-flex xs3>
              <v-img :src="person.headshot" height="100%" width="100%"></v-img>
            </v-flex>
            <v-flex xs9>
              <v-layout column pl-4>
                <v-flex title>{{person.name}}</v-flex>
                <v-flex>출생:{{person.birth_date}}</v-flex>
                <v-flex>신장:{{person.height}}</v-flex>
                <v-flex>
                  배우자
                  <v-flex v-for="family in family_member" :key="family">{{family}}</v-flex>
                </v-flex>
                <v-flex>
                  이력사항
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
      state: false,
      movie: {},
      rating: 0,
      video: "",
      directorlist: [],
      writerlist: [],
      castlist: [],
      main_actor: [],
      more: true,
      personDialog: false,
      trailerDialog: false,
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
      info: {
        id: 0,
        title: "",
        average_rating: 0,
        genres: "genres",
        contents: "null",
        poster: ""
      }
    };
  },
  mounted() {
    this.MovieInfomation(this.$route.params.id);
    this.rating = this.$route.params.rating;
    axios
      .get(
        this.$store.state.server + "/api/movies/?id=" + this.$route.params.id
      )
      .then(res => {
        this.info = res.data[0];
      });
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
      this.personDialog = true;
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
      if(this.career.length > 300)
        this.career = this.career.substring(0,300)+"...";
      this.person.birth_date = this.person.birth_date.substring(0, 10);
    },
    CastMore() {
      this.more = false;
    },
    submit() {
      axios.post(this.$store.state.server + "/api/ratings/", {
        userid: this.$session.get("id"),
        movieid: this.info.id,
        rating: this.rating,
        timestamp: "123456789"
      });
    },
    turnState() {
      if (this.state) this.state = false;
      else this.state = true;
    },
    Viewtrailer() {
      this.trailerDialog = true;
    }
  }
};
</script>

<style>
.base {
  width: 95%;
  height: 90%;
}
.vi{
  border-style: solid;
  border-radius: 10px;
  border-width: 0px 7px 7px 0px;
}
</style>