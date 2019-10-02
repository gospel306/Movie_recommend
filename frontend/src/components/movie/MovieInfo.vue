<template>
  <v-container column justify-content="space-between">
    <v-layout>
      <v-flex xs9>
        <h1>{{movie.title}}</h1>
        <v-flex>
          <v-layout>
            <h3>평점 -</h3>
            <v-rating
              :value="rating"
              color="indigo"
              background-color="indigo"
              half-increments
              dense
              readonly
            />
            <div class="grey--text ml-4">{{ rating.toFixed(1) }}</div>
          </v-layout>
        </v-flex>
        <v-flex>
          <v-layout>
            <h3>장르 -</h3>
            {{movie.genres}}
          </v-layout>
        </v-flex>

        <v-flex>
          <v-layout>
            <h3>감독 -</h3>
            <v-flex v-for="director in directorlist" :key="director.id">
              <a @click="PersonInfo(director.id)">{{director.name}}</a>
            </v-flex>
          </v-layout>
        </v-flex>

        <v-flex>
          <v-layout>
            <h3>작가 -</h3>
            <v-flex v-for="writer in writerlist" :key="writer.id">
              <a @click="PersonInfo(writer.id)">{{writer.name}}</a>
            </v-flex>
          </v-layout>
        </v-flex>

        <v-flex>
          <v-layout>
            <h3>출연진</h3>
            <a v-if="more" @click="CastMore" pl-4>더 보기</a>
          </v-layout>
          <v-layout row>
            <v-flex v-if="more" row pl-4>
              <v-flex v-for="cast in main_actor" :key="cast.id" pa-2>
                <a @click="PersonInfo(cast.id)">{{cast.name}}</a>
              </v-flex>
            </v-flex>
            <v-flex v-else row>
              <v-flex v-for="cast in castlist" :key="cast.id" pa-2>
                <a @click="PersonInfo(cast.id)">{{cast.name}}</a>
              </v-flex>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-flex>

      <v-flex xs3>
        <v-card
          :color="active ? undefined : 'grey lighten-1'"
          class="ma-4"
          height="400"
          width="300"
        >
          <v-img :src="movie.poster" height="450"></v-img>
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
      career: []
    };
  },
  mounted() {
    this.MovieInfomation(this.$route.params.id);
    this.rating = this.$route.params.rating;
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