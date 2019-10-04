<template>
  <div>
    <v-row justify="center">
      <v-btn color="primary" class="ma-2" dark @click="dialog = true; searchUser(id)">상세보기</v-btn>
      <v-btn v-if="check" color="primary" class="ma-2" dark @click="similarMovie(id)">유사영화</v-btn>
      <v-btn v-if="$store.state.login==true && $session.get('id')!='admin'" v-on="on" color="primary" class="ma-2" dark @click="dialog2 = true">평점부여</v-btn>
      <v-dialog
        v-model="dialog"
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable
        max-width="500px"
      >
        <v-card tile>
          <v-toolbar flat dark color="primary">
            <v-toolbar-title>영화 상세정보</v-toolbar-title>
            <div class="flex-grow-1" />
            <v-toolbar-items>
              <v-btn icon dark @click="dialog = false">
                <v-icon>close</v-icon>
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-card-text>
            <v-list three-line subheader>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>영화 제목</v-list-item-title>
                  <v-list-item-subtitle>{{ title }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>영화 장르</v-list-item-title>
                  <v-list-item-subtitle>{{ genreSplit }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>영화 평점</v-list-item-title>
                  <v-list-item-subtitle>{{ ratingRounds }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>

            <v-divider />
            <v-list three-line subheader>
              <v-subheader>해당 영화를 본 사람들</v-subheader>
              <v-list disabled dense sm5 md5 lg5>
                <v-list-item v-for="(item, i) in items" :key="i" @click="() => {}">
                  <v-list-item-content>
                    <v-list-item-title>{{ item.username }}</v-list-item-title>
                    <v-list-item-subtitle>{{ item.gender }}, {{ item.age }}, {{ item.occupation }}</v-list-item-subtitle>
                    <v-list-item-subtitle>{{ item.rating }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-list>
          </v-card-text>

          <div style="flex: 1 1 auto;" />
        </v-card>
      </v-dialog>
      <v-dialog v-model="dialog2" persistent max-width="300">
        <v-card>
          <v-layout justify-center>
            <v-card-title class="headline">이 영화의 점수는?</v-card-title>
          </v-layout>
            <v-card-text>
                <v-layout justify-center>별점을 매겨주세요!</v-layout>
            </v-card-text>
          <v-layout justify-center>
          <v-rating
            v-model="newRating.rating"
            color="indigo"
            background-color="indigo"
          />
          </v-layout>
          <v-card-actions>
            <div class="flex-grow-1"></div>
            <v-btn color="green darken-1" text @click="submit()">완료</v-btn>
            <v-btn color="green darken-1" text @click="dialog2 = false">취소</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    check:{
      type: Boolean,
      default : true,
    }
  },
  data() {
    return {
      dialog: false,
      dialog2: false,
      newRating:{
        userid:this.$session.get('id'),
        movieid:this.id,
        rating:"",
        timestamp:"123456789"
      },
      items: []
    };
  },
  computed: {
    genreSplit() {
      var str = this.genres;
      return str.replace(/\|/g, " / ");
    },
    ratingRounds() {
      var num = this.rating;
      return num.toFixed(2);
    }
  },
  methods: {
    searchUser: function(id) {
      axios
        .get(this.$store.state.server + "/api/auth/signup-many/?movieid=" + id)
        .then(res => {
          this.items = res.data;
        });
    },
    similarMovie(id){
      this.$router.push({name: 'moviesimilar', params:{'id': id}});
    },
    postRating(){
      newRating.movieid = item.id;
    },
    submit(){
      axios.post(this.$store.state.server + "/api/ratings/", this.newRating);
      this.dialog2 = false;
    }
  },
  
};
</script>