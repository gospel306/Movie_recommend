<template>
  <v-container column justify-content="space-between">
    <v-layout>
      <v-flex xs8>
        <h1>{{this.info.title}}</h1>
        <v-flex>
          <v-layout>
            <h3>평점 :</h3>
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
            <h3>장르 :</h3>
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
      <v-flex xs4>
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
      {{this.info.contents}}
    </v-layout>

    
  </v-container>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      info:{
        id: 0,
        title: "",
        average_rating: 0,
        genres: "genres",
        contents: "null",
        poster: ""
      },
      rating:0,
      dialog:false,
    };
  },
  mounted(){
    axios.get(this.$store.state.server+"/api/movies/?id="+this.$route.params.id).then(res=>{
      console.log(res)
      this.info = res.data[0]
    }).catch(e=>{
      console.log(e)
    })
  },
  methods:{
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